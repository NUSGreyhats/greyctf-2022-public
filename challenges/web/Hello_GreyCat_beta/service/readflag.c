#include <stdio.h>

#include <string.h>

int main(int argc, char * argv[]) {
    char buf[64];
    FILE * fptr;

    if ((fptr = fopen("/flag.txt", "r")) == NULL) {
        printf("Error! opening file");
        return -1;
    }

    fgets(buf, 64, fptr);
    puts(buf);
    fclose(fptr);

    return 0;
}
