#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <signal.h>
#include <time.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

#include "rc4.h"

typedef unsigned long long ull;

#define _DEBUG

// char key[33] = hide("\x91", "visithttp://youtu.be/dQw4w9WgXcQ\0");
char key[33] = "\x91\xe7\x8e\xfd\x94\xe0\x88\xfc\x88\xf8\xc2\xed\xc2\xbb\xd4\xa1\xd5\xa0\x8e\xec\x89\xa6\xc2\x93\xe4\xd0\xa7\x9e\xc9\xae\xf6\x95\xc4";


// char lyrics[] = 
//     "Never gonna give you flag\n"
//     "Never gonna let you down\n"
//     "Never gonna run around and desert you\n"
//     "Never gonna make you cry\n"
//     "Never gonna say goodbye\n"
//     "Never gonna tell a lie and hurt you\n"
//     "flag{<3_N3v3r_G0nn4_G1v3_u_Up_<3}\n"
//     "We've known each other for so long\n"
//     "Your heart's been aching, but you're too shy to say it (to say it)\n"
//     "Inside, we both know what's been going on (going on)\n"
//     "We know the game and we're gonna play it\n\0";

// unhide2(rc4(lyrics))
char lyrics[] = "\xab\x4\x99\xe\x6f\xbd\xf9\x7f\x80\x6c\x0\x76\x39\x6d\xf2\xc1\xd6\xe\xb2\xe5\xf0\x8\x28\xe4\x32\x6f\x51\x1b\x43\x70\x41\x9e\x6b\xf7\xaf\x8b\x25\xa8\x43\xf\x2\x9d\xd\xfa\x71\xa5\x49\x3d\x75\xec\xab\xbd\x97\xe6\x6a\xc6\xf7\x64\x31\x57\x1d\x8d\xac\x34\x51\xc0\x52\x5e\xf0\x5c\xe0\x3c\x65\x42\x1f\xfe\x74\xab\xba\xd8\xe5\xb4\x5d\x12\x93\x64\x90\x2d\xc7\xed\x83\x52\x82\xc2\x7e\x7e\x1a\x79\x83\x6e\xd0\x38\x26\xe0\xae\xa6\x94\xa6\x81\x59\x23\xe4\xd8\x5d\xd6\xcc\x7\x7c\x80\x56\xca\x9d\xa3\x4a\x79\xf6\xda\x4c\xc5\x39\x3e\xb\xfc\x73\xf4\xf9\xac\xcf\x3\x5e\xba\xbf\x52\xdf\xaf\x2a\x5\x7c\x66\xbc\x85\x24\xe\x9f\x7c\x38\x51\xd5\x22\x9c\xeb\x49\xb3\x6\xb4\xa\x2c\x63\xc4\x1c\x41\x77\x90\x62\xfa\x70\xb\xaa\x58\xf5\x92\x52\xd7\x91\xd0\xca\x80\xfd\x6\x2b\xda\x39\xf9\x9\x4c\x26\x38\x74\xf8\xd7\x97\x99\xad\xea\xad\x8a\x84\x23\xab\x3f\x91\x91\xaf\x5f\x5c\xec\xf0\xa0\x48\x22\x29\x7d\xdc\x19\x7\x35\xfa\xca\x3c\xdc\x7f\x60\x87\x4a\x28\xbd\x8b\x33\x4\xa3\x32\x22\xe2\x1d\x39\xeb\xb3\xe9\x9a\x21\x4a\x37\x71\xcc\xa2\x10\x7\x88\x1e\x1d\x32\x10\x2b\x7c\x7\xb\x6a\x43\x3d\x42\xc1\x2f\xb5\x25\xe\xa\xd0\x5\x9\xa2\x81\x11\xbd\x13\x31\x58\x35\xd7\x12\xf9\x40\x8a\x42\xd3\x45\xf6\x2e\x1b\x18\xbd\xb\x17\x4\xe6\x5c\x4e\xe6\x28\x16\xa8\x98\x54\x41\xe\x55\xe4\x15\xeb\x15\x37\x20\xfe\xe5\xee\x22\xbb\xb1\xcc\x26\xcd\x8\x25\x7b\xcb\x3\x8c\xeb\xa2\x9c\x3d\x36\xff\xd7\xa6\xc1\xf3\xf7\xcb\xe8\x55\xfc\xe1\xfd\xc1\x80\x1b\x84\xb6\x43\xf\x3c\x3c\x50\xae\xe8\xbc\xc3\x54\x32\x9c\x2\x7e\x8d\xd\x80\xee\xd7\xe3\x8f\x7c\xe8\x7\xdc\x38\x16\x22\x51\x3d\x20\xf4\x41\xcf\xe0\x2e\x82\xc7\xd1\x59\xbc\x23\xed\x5a\xb2\x2b\x13\xbb";

int lyric_len = sizeof(lyrics);

time_t start, end;

char x(char volatile a, char volatile b) {
    return ((~((((~a) & 0xFF) | b) & (a | ((~b) & 0xFF)))) & 0xFF) & (((~((((~a) & 0xFF) | b) & (a | ((~b) & 0xFF)))) & 0xFF) | (char)(0xB7F748F3));
}

void dputs(const char *str) {
    #ifdef _DEBUG
    puts(str);
    #endif
}

char* hide(char iv, char *p, char *out, int len) {
    out[0] = iv;
    for (int i=1; i < len+1; i++) {
        out[i] = x(out[i-1], p[i-1]);
    }

    return out;
}

void phex(char *str, int len) {
    #ifdef _DEBUG
    for (int i=0; i<len; i++) {
        printf("\\x%hhx", str[i]);
    }
    #endif
}

void unhide2(char *p, char *out, int len) {
    for (int i=0; i<len; i++) {
        out[i] = ((p[i] & 0x0F) << 4) | (p[i] >> 4) & 0x0F;
    }
}

char* unhide(char* ctx, char* out, int len) {
    for (int i=1; i<len; i++) {
        out[i-1] = x(ctx[i-1], ctx[i]);
    }
    out[len-1] = '\0';
    return out;
}


ull fib(ull n) {
    if (n==0 || n==1) return 1;
    return fib(n-1) + fib(n-2);
}

void realmain() {
    fib(42); // meaning of life

    char buf[500];
    if (!read(0, buf, 500)) { exit(1); };

    time_t end = time(0);
    // printf("time taken: %ld %ld %ld\n", end, start, end-start);
    if (end - start < 1 || end-start > 10) {
        // dputs("too soon or too fast");
        exit(1);
    }
    // dputs("checking user input:");

    RC4(key, buf, buf, sizeof(lyrics));
    unhide2(buf, buf, sizeof(lyrics));
    
    // last few bytes gets corrupted for some reason, can't be bothered to figure out since it's non-consequential.
    for (int i=0; i<sizeof(lyrics)-4; i++) {
        if (lyrics[i] != buf[i]) {
            // puts("That's not what I want to hear!");
            exit(1);
        }
    }

}

void segfault_handler(int signo) {
    realmain();
    exit(0);
}



bool __attribute__ ((constructor)) initialize() {
    signal(SIGSEGV, segfault_handler);
    start = time(0);
    puts("I want a song:");
    return false;
}

int main(int argc, char *argv[]) {
    unhide(key, key, 33);
    // junk and trigger segfault
    asm("lea -4(%eax), %eax");
    asm("push %eax");
    asm("lea -4(%eax), %eax");
    asm("pop %eax");
    asm("xor %eax, %eax");
    asm("mov -4(%ebx), %eax");
    asm("call *%eax");
    return 0;
}
