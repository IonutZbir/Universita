/*
Creare un programma che che legge un file e conta le occorenze di una parola nel seguente modo:
    - Il primo processo legge dall'inzio alla metà e conta le occorenze della parola.
    - Il secondo processo legge dalla metà fino alla fine e conta le occorenze dell parola.
    - Inviano poi il numero di occorenze al processo padre, il quale le somma e le stampa a video.
*/

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define TRUE 1
#define RD_PIPE 0
#define WR_PIPE 1

int str_equals(const char *str1, char *str2) {
    printf("[INFO]: %s - %s\n", str1, str2);
    if (strcmp(str1, str2) == 0) {
        return 1;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    int first_pipe[2], second_pipe[2];
    pipe(first_pipe);
    pipe(second_pipe);

    int first_pid, second_pid;
    int first_fd, second_fd;

    struct stat file_info; // non inizializzi la stat

    const char *file_name = argv[2];
    const char *word_to_find = argv[1];

    int len = strlen(word_to_find);

    // char *buffer = (char *)malloc(sizeof(char) * 9);

    stat(file_name, &file_info);

    int file_size = file_info.st_size;
    const int half = file_size / 2;

    first_pid = fork();

    if (first_pid == 0) {
        int i = 0, count = 0;
        first_fd = open(file_name, O_RDONLY);
        close(first_pipe[RD_PIPE]);
        char buffer[len + 1];

        while (i <= half) {
            read(first_fd, buffer, sizeof(buffer));
            buffer[len] = '\0';
            count += str_equals(word_to_find, buffer);
            i++;
            lseek(first_fd, i, SEEK_SET);
        }

        write(first_pipe[WR_PIPE], &count, sizeof(count));
        close(first_fd);
        exit(0);
    } else if (first_pid > 0) {
        second_pid = fork();
        if (second_pid == 0) {
            char buffer[len + 1];
            int count = 0, i = half;
            second_fd = open(file_name, O_RDONLY);
            close(second_pipe[RD_PIPE]);

            while ((i + len) <= file_size) {
                lseek(second_fd, i, SEEK_SET);
                read(second_fd, buffer, sizeof(buffer));
                buffer[len] = '\0';
                count += str_equals(word_to_find, buffer);
                i++;
            }

            write(second_pipe[WR_PIPE], &count, sizeof(count));
            close(second_fd);
            exit(1);
        } else if (second_pid > 0) {

            int f, s;
            close(first_pipe[WR_PIPE]);
            close(second_pipe[WR_PIPE]);
            waitpid(first_pid, NULL, 0);
            read(first_pipe[RD_PIPE], &f, sizeof(f));
            waitpid(second_pid, NULL, 0);
            read(second_pipe[RD_PIPE], &s, sizeof(s));

            int final = f + s;
            printf("%s compare %d volte all'interno del file %s\n", argv[1], final, argv[2]);
            return 0;
        }
    }
}
