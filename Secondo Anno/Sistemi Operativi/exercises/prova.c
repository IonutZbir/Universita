#include <inttypes.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUFFER_SIZE 11

int buffer[BUFFER_SIZE] = {0};
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void print_buffer() {
    printf("[");
    for (int i = 0; i < BUFFER_SIZE; i++) {
        printf("%2d,", buffer[i]);
    }
    printf("]\n");
}

void *writePlusOne(void *arg) {
    while (1) {
        sleep(rand() % 4); // Attende un numero di secondi random tra 0 e 3

        pthread_mutex_lock(&mutex);

        int index = rand() % BUFFER_SIZE;
        buffer[index] = 1;

        print_buffer();

        pthread_mutex_unlock(&mutex);
    }

    return NULL;
}

void *writeMinusOne(void *arg) {
    while (1) {
        sleep(rand() % 4); // Attende un numero di secondi random tra 0 e 3

        pthread_mutex_lock(&mutex);

        int index = rand() % BUFFER_SIZE;
        buffer[index] = -1;

        print_buffer();

        pthread_mutex_unlock(&mutex);
    }

    return NULL;
}

void *checkBuffer(void *arg) {
    while (1) {
        sleep(rand() % 4); // Attende un numero di secondi random tra 0 e 3

        pthread_mutex_lock(&mutex);

        int allInitialized = 1;
        for (int i = 0; i < BUFFER_SIZE; ++i) {
            if (buffer[i] == 0) {
                allInitialized = 0;
                break;
            }
        }

        if (allInitialized) {
            int countPlusOne = 0;
            int countMinusOne = 0;

            for (int i = 0; i < BUFFER_SIZE; ++i) {
                if (buffer[i] == 1) {
                    countPlusOne++;
                } else if (buffer[i] == -1) {
                    countMinusOne++;
                }
            }

            if (countPlusOne > countMinusOne) {
                pthread_mutex_unlock(&mutex);
                pthread_exit(NULL);
            }
        }

        pthread_mutex_unlock(&mutex);
    }

    return NULL;
}

int main() {
    srand(time(NULL));

    pthread_t thread1, thread2, thread3;

    pthread_create(&thread1, NULL, writePlusOne, NULL);
    pthread_create(&thread2, NULL, writeMinusOne, NULL);
    pthread_create(&thread3, NULL, checkBuffer, NULL);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_join(thread3, NULL);

    return 0;
}
