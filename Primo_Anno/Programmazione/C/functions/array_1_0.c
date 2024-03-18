#include <stdio.h>
#include <stdlib.h>


/*
---------------------------------------
    Lista Prototipi
*/
int sum(int arr[], int len);
void store(int arr[], int len);
void print_arr(int arr[], int len);
void reverse(int arr[], int len);
int min(int arr[], int len);
int max(int arr[], int len);
int *extend(int *arr_a, int *arr_b, int len_a, int len_b);
int *copy(int *arr, int len);
int *append(int *arr, int len, int elem);

/*
    Lista Prototipi
---------------------------------------
*/

void main(){
    int a[] = {165, 265, 354, 4543, 32, 58, 2312};
    int b[] = {6, 7, 8, 9, 10};
    int *c;
    int len_a = sizeof(a) / sizeof(int);
    int len_b = sizeof(b) / sizeof(int);
    c = extend(a, b, len_a, len_b);
    print_arr(c, len_a + len_b);
    
}

// array_int init(array_int arr){
    
// }


int *extend(int *arr_a, int *arr_b, int len_a, int len_b)
{
    int len_c = len_a + len_b;
    int *arr_c = malloc((len_c) * sizeof(int));
    if (arr_c != NULL)
    {
        for (int i = 0; i < len_a; i++)
        {
            arr_c[i] = arr_a[i];
        }
        for (int j = 0; j < len_b; j++)
        {
            arr_c[j + len_a] = arr_b[j];
        }
    }
    return arr_c;
}

int *copy(int *arr, int len){
    int *new_arr = malloc(len * sizeof(int));
    if (new_arr != NULL)
    {
        for (int i = 0; i < len; i++)
        {
            new_arr[i] = arr[i];
        }
    }
    return new_arr;
}

int *append(int *arr, int len, int elem){
    int *new_arr = malloc((len + 1) * sizeof(int));
    if (new_arr != NULL)
    {
        for (int i = 0; i < len; i++)
        {
            new_arr[i] = arr[i];
        }
        new_arr[len] = elem;
    }
    return new_arr;
}

void store(int arr[], int len){
    for(int i = 0; i<len; i++){
        scanf("%d", &arr[i]);
    }
}

void print_arr(int arr[], int len){
    for(int i = 0; i < len; i++){
        printf("%d -> %d\n", i, arr[i]);
    }
}

void reverse(int arr[], int len){
    for(int i = len - 1; i >= 0; i--){
        printf("%d -> %d\n", i, arr[i]);
    }
}

int sum(int arr[], int len){
    int sum =  0;
    for(int i = 0; i < len; i++){
        sum += arr[i];
    }
    return sum;
}

int min(int arr[], int len){
    int min =  arr[0];
    for(int i = 0; i < len; i++){
        if(arr[i] <= min)
            min = arr[i];
    }
    return min;
}

int max(int arr[], int len){
    int max =  arr[0];
    for(int i = 0; i < len; i++){
        if(arr[i] >= max)
            max = arr[i];
    }
    return max;
}