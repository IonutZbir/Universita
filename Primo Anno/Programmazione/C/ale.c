#include <stdio.h>

void GeneraSeqBin(int n) {
    int numSeq = 1 << n; //shifta a sinistra n volte 
    
    // ciclo
    for (int i = 0; i < numSeq; i++) {
        // prende la sequenza binaria
        for (int j = n - 1; j >= 0; j--) {
            int bit = (i >> j) & 1; // Estrae il bit nella posizione j
            printf("%d", bit);
        }
        printf("\n");
    }
}


void main() {
    int n;
    printf("lunghezza: ");
    scanf("%d", &n);
    printf("Sequenze binarie di lunghezza %d:\n", n);
    GeneraSeqBin(n);
}