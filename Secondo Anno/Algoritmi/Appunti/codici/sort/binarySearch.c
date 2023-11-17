#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int binarySearch(int* arr, int n, int start, int end){
	if (start > end) return -1;
	int m = (start + end) / 2;
	if (arr[m] == n) return m;
	if (arr[m] > n) return binarySearch(arr, n, start, m - 1);
	else return binarySearch(arr, n, m + 1, end);
}

int main(){
	int a[] = {1, 3, 3, 5, 5, 4, 10, 20};
	printf("il numero sta nella posizione:%d\n", binarySearch(a, 3, 0,8));
}
