#include <stdio.h>

#include <string.h>

int main(int argc, char * argv[]) {
    char buf[64];
    FILE * fptr;
    char *tmp = "P4s5_w0Rd";
    char password[] = {
        tmp[2],
        tmp[7],
        tmp[0],
        tmp[8],
        tmp[1],
        tmp[3],
        tmp[5],
        tmp[4],
        tmp[6],
        0
    };

    if (argc < 2) {
        puts("Password requried!");
        return -1;
    }

    if (strcmp(password, argv[1])) {
        puts("Wrong Password!");
        return -1;
    }

    if ((fptr = fopen("/flag.txt", "r")) == NULL) {
        printf("Error! opening file");
        return -1;
    }

    fgets(buf, 64, fptr);
    puts(buf);
    fclose(fptr);

    return 0;
}
