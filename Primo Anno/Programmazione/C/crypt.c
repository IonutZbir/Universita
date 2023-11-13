#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void crypt_veg(char* mess, char* key){
    int n, r, a, b, L = 26, i = 0, j = 0, len_str = strlen(mess);
    char *crypted = malloc((len_str + 1) * sizeof(char));
    assert(strlen(key) != 0);
    while ((mess[i] != '\0' || key[j] != '\0') && i < len_str)
    {
        if(key[j] == '\0'){
            j = 0;
        }
        a = mess[i] - 'A';
        b = key[j] - 'A';
        n = a + b;
        r = n % L;
        crypted[i] = r + 'A';
        i++;
        j++;
    }
    crypted[i] = '\0';
    strcpy(mess, crypted);
    free(crypted);    
}

void decrypt_veg(char* mess, char* key){
    int n, r, a, b, L = 26, i = 0, j = 0, len_str = strlen(mess);
    char *crypted = malloc((len_str + 1) * sizeof(char));
    assert(strlen(key) != 0);
    while ((mess[i] != '\0' || key[j] != '\0') && i < len_str)
    {
        if(key[j] == '\0'){
            j = 0;
        }
        a = mess[i] - 'A';
        b = key[j] - 'A';
        n = a - b + L;
        r = n % L;
        crypted[i] = r + 'A';
        i++;
        j++;
    }
    crypted[i] = '\0';
    strcpy(mess, crypted);
    free(crypted);     
}


void main(){
    char mess[] = "RAPPORTOIMMEDIATO";
    char key[] = "VERME";
    crypt_veg(mess, key);
    printf("%s\n", mess);
    decrypt_veg(mess, key);
    printf("%s\n", mess);
}