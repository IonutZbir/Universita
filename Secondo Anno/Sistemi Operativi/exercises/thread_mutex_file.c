/*
1.  Il programma crea un file chiamato dati.txt" contenente un array di 10 numeri interi, inizializzati a zero.
    Ogni numero deve essere separato da uno spazio.
2.  Genera tre thread utilizzando le librerie POSIX:
    • Il primo thread legge il contenuto del file "dati.txt", incrementa ogni numero di una cella e
    scrive i nuovi valori nel file.
    Il thread esegue questa operazione in un ciclo infinito con una pausa casuale tra le iterazioni.
    • Il secondo thread legge il contenuto del file "dati.txt", decrementa ogni numero di una cella e
    scrive i nuovi valori nel fie.
    Il thread esegue questa operazione in un ciclo infinito con una pausa casuale tra le iterazioni.
    • Il terzo thread, in un ciclo infinito, controlla se tutti i valori nel file sono diventati positivi.
    In caso affermativo, termina entrambi i thread.
4.  Assicurati che un thread abbia accesso esclusivo al file mentre legge o scrive. Utilizza I mutex per gestire
    l'accesso concorrente al file.
5.  Introduci una pausa casuale tra le operazioni di lettura e scrittura del thread.
*/

#include <fcntl.h>
#include <math.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

#define N 10
#define OUTPUT_MODE 0700

pthread_mutex_t the_mutex;
pthread_cond_t condp;
pthread_t p1, p2, p3;

const char file_name[] = "dati.txt";

int write_file(int *buffer, int len) {
    int file = creat(file_name, OUTPUT_MODE);
    if (file < 0)
        return -1;
    char buff[3] = {0};

    for (int i = 0; i < len; i++) {
        buff[0] = buffer[i] + '0';
        buff[1] = ' ';
        buff[2] = '\0';
        write(file, &buff, strlen(buff));
    }
    close(file);
    return 0;
}

int modify_file(int index) {
    struct stat info;
    int size = info.st_size, file, number;

    if (stat(file_name, &info) < 0)
        return -1;

    lseek(file, index * 2, SEEK_SET);
    file = open(file_name, O_RDONLY);
    read(file, &number, 1);
    close(file);

    file = open(file_name, O_WRONLY);
    lseek(file, index * 2, SEEK_SET);
    number++;
    write(file, &number, 1);
    close(file);

    return 0;
}

void print_data() {
    struct stat info;
    int size = info.st_size, file;
    char buffer[size];
    file = open(file_name, O_RDONLY);
    read(file, &buffer, size);
    printf("[");
    for (int i = 0; i < size; i++) {
        if (buffer[i] != ' ') {
            printf("%3d ", buffer[i]);
        }
    }
    printf("]\n");
    close(file);
}

void *increment(void *args) {
    int index;
    while (1) {
        pthread_mutex_lock(&the_mutex);
        index = rand() % N;
        modify_file(index);
        print_data();
        pthread_cond_signal(&condp);
        pthread_mutex_unlock(&the_mutex);
    }
}

int main() {
    int buffer[N] = {0};
    if (write_file(buffer, N) < 0) {
        fprintf(stderr, "[ERROR]: Could not write on file\n");
        return -1;
    }

    pthread_create(&p1, NULL, increment, NULL);
    pthread_join(p1, NULL);
    pthread_mutex_destroy(&the_mutex);
    pthread_cond_destroy(&condp);
    return 0;
}
