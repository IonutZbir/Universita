/*
 * Progettare un algoritmo (efficiente) che, dato un array ordinato
 * A[1:n] di n interi e un intero x, trova (se esistono) due indici i e j,
 * i<j, tale che A[i]+A[j]=x.
 */

#include <stdio.h>
#include <stdlib.h>
#define ARRAY_SIZE(array) (sizeof(array) / sizeof(array[0]))

typedef struct array {
    int len;
    int *data;
} array;

int binarySearch(int *arr, int n, int start, int end) {
    if (start > end)
        return -1;
    int m = (end + start) / 2;
    if (arr[m] == n)
        return m;
    if (arr[m] > n)
        return binarySearch(arr, n, start, m - 1);
    else
        return binarySearch(arr, n, m + 1, end);
}

int *soluzione1(array a, int x) {
    // soluzione banale, in tempo quadratico
    int *output = malloc(sizeof(int) * 2);
    for (int i = 0; i < a.len - 1; i++) {
        for (int j = i + 1; j < a.len; j++) {
            if (a.data[i] + a.data[j] == x) {
                output[0] = i;
                output[1] = j;
                return output;
            }
        }
    }
    output[0] = -1;
    output[1] = -1;
    return output;
}

int *soluzione2(array a, int x) {
    // soluzione meno  banale, in tempo n log n
    int *output = malloc(sizeof(int) * 2);
    int y; // incognita
    int j; // indice incognita
    for (int i = 0; i < a.len - 1; i++) {
        y = x - a.data[i];
        j = binarySearch(a.data, y, 0, a.len);
        if (j > -1) {
            output[0] = i;
            output[1] = j;
            return output;
        }
    }
    output[0] = -1;
    output[1] = -1;
    return output;
}

int *soluzione3(array a, int x) {
    // soluzione lineare, efficiente
    int i = 0;
    int j = a.len - 1;
    int *output = malloc(sizeof(int) * 2);
    while (i < j) {
        if (a.data[i] + a.data[j] == x) {
            output[0] = i;
            output[1] = j;
            return output;
        }
        if (a.data[i] + a.data[j] < x)
            i++;
        else
            j--;
    }
    output[0] = -1;
    output[1] = -1;
    return output;
}

int main() {
    int x = 20; // 26
    int a[] = {
        1,
        2,
        34,
    };
    array v;
    v.len = ARRAY_SIZE(a);
    v.data = malloc(v.len * sizeof(int));

    for (int i = 0; i < v.len; i++) {
        v.data[i] = a[i];
    }

    int *res1 = soluzione1(v, x);
    int *res2 = soluzione2(v, x);
    int *res3 = soluzione3(v, x);

    printf("SOLUZIONE 1: %d, %d\n", res1[0], res1[1]);
    printf("SOLUZIONE 2: %d, %d\n", res2[0], res2[1]);
    printf("SOLUZIONE 3: %d, %d\n", res3[0], res3[1]);

    return 0;
}
