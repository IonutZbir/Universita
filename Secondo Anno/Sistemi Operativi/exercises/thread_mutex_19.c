/*
Scrivere un programma C che segue le seguenti specifiche.
Il processo eseguito, inizialmente crea un buffer come array di 11 numeri interi, inizializzati a zero.
In seguito genera tre thread utilizzando le librerie POSIX secondo le seguenti specifiche:
•   Il primo thread sceglie casualmente una cella del buffer e vi scrive il numero +1,
    qualsiasi sia il valore presente nella cella.
•   Il secondo thread sceglie casualmente una cella del buffer e vi scrive il numero -1,
    qualsiasi sia il valore presente nella cella.
•   Il terzo thread controlla se tutte le celle del buffer sono state inizializzate.
    In caso positivo, determina se il numero di celle contententi un valore pari a +1 è maggiore di quelle con -1
    e termina tutti e tre i thread.
•  Mentre un thread ha accesso al buffer, nessun altro thread deve accedervi.
•  Una volta che un thread ha acceduto in lettura o scrittura al buffer,
   deve attendere un numero di secondi random tra 0 e 3
*/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define N 11

pthread_mutex_t the_mutex;
pthread_cond_t cond_control;

int buffer[N] = {0};

void print_buffer() {
    printf("[");
    for (int i = 0; i < N; i++) {
        printf("%2d,", buffer[i]);
    }
    printf("]\n");
}

void *set_one(void *args) {
    while (1) {
        pthread_mutex_lock(&the_mutex);
        int index = rand() % N;
        buffer[index] = 1;
        printf("[INFO]: p1 genera: %d\n", index);
        print_buffer();
        sleep(rand() % 4);
        pthread_mutex_unlock(&the_mutex);
    }
    return NULL;
}

void *set_neg_one(void *args) {
    while (1) {
        pthread_mutex_lock(&the_mutex);
        int index = rand() % N;
        buffer[index] = -1;
        printf("[INFO]: p2 genera: %d\n", index);
        print_buffer();
        sleep(rand() % 4);
        pthread_mutex_unlock(&the_mutex);
    }
    return NULL;
}

void *control(void *args) { // Correggi la firma della funzione

    while (1) {
        pthread_mutex_lock(&the_mutex);
        int o = 0, n = 0;

        int allInitialized = 1;
        for (int i = 0; i < N; ++i) {
            if (buffer[i] == 0) {
                allInitialized = 0;
                break;
            }
        }

        if (allInitialized) {

            for (int i = 0; i < N; i++) {
                if (buffer[i] == 1)
                    o++;
                if (buffer[i] == -1)
                    n++;
            }

            if ((n + o) == N) {
                if (o > n) {
                    printf("[INFO]: Ha vinto il thread 1, impostando %d uno\n", o);
                } else {
                    printf("[INFO]: Ha vinto il thread -1, impostando %d -uno\n", n);
                }
                pthread_mutex_unlock(&the_mutex);
                pthread_exit(NULL); // Termina il thread
            }
        }
        printf("[INFO]: sono il 3 thread\n");
        sleep(rand() % 4);
        pthread_mutex_unlock(&the_mutex);
    }
    return NULL;
}
int main() {

    srand(time(NULL));
    int ret_control;

    pthread_t p1, p2, p3;
    pthread_mutex_init(&the_mutex, NULL);
    pthread_cond_init(&cond_control, NULL);

    pthread_create(&p1, NULL, set_one, NULL);
    pthread_create(&p2, NULL, set_neg_one, NULL);
    pthread_create(&p3, NULL, control, NULL);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(p3, NULL);

    pthread_cond_destroy(&cond_control);
    pthread_mutex_destroy(&the_mutex);
    return 0;
}
