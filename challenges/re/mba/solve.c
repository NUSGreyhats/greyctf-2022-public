#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>

#include "hash.h"

int main() {

    unsigned long target = 0x3dd99b6c9d29c576;

    unsigned long seed = 0x5ca1ab1ef01dab1e;

    unsigned long pass = seed ^ target;

    char password[9] = {0};

    for (int i=0; i<8; i++) {
        password[8-i] = pass&0xff;
        pass = pass >> 8;
    }

    password[0] = password[8];
    password[8] = '\0';

    printf("%s\n", password);
}