#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define CONTENT_SZ 0x28
#define BY_SZ 0x10

typedef unsigned long long num;

typedef struct Report {
    char content[CONTENT_SZ];
    char by[BY_SZ];
} Report;

Report* reports;
num len;

num read_num() {
    char buf[0x20];
    int ret = read(0, buf, 0x20);

    if (ret == -1) {
        printf("read failed");
        exit(-1);
    }

    return strtoull(buf, NULL, 0);
}

void alloc() {
    printf("How many reports? ");
    num nlen = read_num();
    if (nlen <= len) {
        return;
    }
    num alloc_size = nlen * sizeof(Report);

    // Steve Wozniak:
    // disallow allocs above a PAGE_SIZE
    // if the programmer after me is dumb,
    // he might cause an out of bounds, don't
    // want that the allocation to border libc
    if (alloc_size > 0x1000) {
        printf("allocation too big!");
        exit(-1);
    }

    Report* new_reports = (Report*)malloc(alloc_size);
    memset(new_reports, 0, nlen * sizeof(Report));
    if (reports) {
        memcpy(new_reports, reports, len * sizeof(Report));
        free(reports);
    }
    reports = new_reports;
    len = nlen;
}

void get(num idx) {
    printf("Report #%lld (by %s):\n\t%s\n", idx, reports[idx].by, reports[idx].content);
}

void set(num idx) {
    printf("---- Report #%lld ----\n", idx);
    printf("By: ");
    read(0, reports[idx].by, BY_SZ);
    printf("Content: ");
    read(0, reports[idx].content, CONTENT_SZ);
}

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

num read_idx() {
    printf("Enter Index: ");
        
    // commit 045e12a:
    // Stop out-of-bounds created by dumb coworkers.
    // Now there is no way to pwn this program.
    // - George Hotz

    num idx = read_num();
    if (idx >= len) {
        printf("out of bounds!");
        exit(-1);
    }
    return idx;
}

int main() {
    setup();

    puts("---- Super Safe Reporting System ----");
    alloc();

    while (1) {
        printf("Option: ");
        num opt = read_num();
        
        switch (opt)
        {
        case 1: {
            alloc();
            break;
        }
        case 2: {
            num idx = read_idx();
            get(idx);
            break;
        }
        case 3: {
            num idx = read_idx();
            set(idx);
            break;
        }
        default:
            break;
        }
    }
}