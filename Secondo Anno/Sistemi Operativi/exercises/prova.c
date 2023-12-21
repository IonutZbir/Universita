#include <stdio.h>

int main() {
    char uno_c = '1';
    int uno_i = 1;

    printf("[INFO]: Da char a int: %c -> %d\n", uno_c, uno_c - '0');
    printf("[INFO]: Da int a char: %d -> %c\n", uno_i, uno_i + '0');

    return 0;
}
