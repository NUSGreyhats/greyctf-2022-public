#include "all.h"
#include <string.h>

char enc[] = "\x0c\x17\x1c\x12\x1e\x1d\x5a\x01\x26\x12\x55\x0c\x34\x10\x0a\x58\x3a\x17\x06\x3a\x49\x19\x3a\x16\x09\x0f\x1d\x1e\x08\x09\x34\x55\x0b\x34\x02\x1d\x09\x3a\x49\x19\x3a\x1e\x03\x0c\x1d\x19\x04\x26\x5b\x17\x26\x19\x0c\x03\x02\x0b\x26\x5b\x17\x26\x02\x01\x18\x34\x55\x0b\x34\x07\x10\x05\x0f\x18\x54\x18";
char key[3] = {};
char dec[sizeof(enc)];

void check()
{
    for (int i = 0; i < sizeof(enc)-1; ++i) {
        dec[i] = enc[i] ^ key[i % 3];
    }

    if (memcmp(dec, "grey", 4)) {
        puts("One of them was wrong :(");
        return;
    }

    printf("Congrats! %s\n", dec);
}

int main()
{
    int ans;

    printf("Tell me the address of the function h12 (in decimal): ");
    scanf("%d", &ans);
    // printf("%d vs %d\n", ans, &h12);
    if (ans == &h12) key[0] = 'k';

    printf("Tell me the address of the function t80 (in decimal): ");
    scanf("%d", &ans);
    // printf("%d vs %d\n", ans, &t80);
    if (ans == &t80) key[1] = 'e';

    printf("Tell me the address of the function g20 (in decimal): ");
    scanf("%d", &ans);
    // printf("%d vs %d\n", ans, &g20);
    if (ans == &g20) key[2] = 'y';

    check();

    return 0;
}