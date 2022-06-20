#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <algorithm>
#include <numeric>
#include <unistd.h>

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

struct block {
    char title[0x20];
    char* content;
    size_t content_len;
    size_t hash;
    block* next;
};

// super secure hash function that java uses
// should be EVEN better than CRC32!!!!
size_t hashb(char* content, size_t content_len) {
    return std::accumulate(content, content + content_len, 0ULL,
        [](auto hash, auto v) { return hash + 31 * v; });
}

block* blockchain;

void menu() {
    puts("1. add");
    puts("2. rmv");
    puts("3. view");
    puts("4. edit");
    printf("> ");
}

char* read_content(size_t* len) {
    printf("Length > ");
    scanf("%zu", len);
    if (*len >= 0x1000) {
        puts("[x] Too big");
        exit(1);
    }
    auto content = (char*)malloc(*len);

    printf("Content > ");
    read(0, content, *len);
    return content;
}

size_t read_hash() {
    size_t hash;
    printf("Hash > ");
    scanf("%zu", &hash);
    return hash;
}

void add() {
    size_t len;
    auto content = read_content(&len);

    auto new_block = (block*)malloc(sizeof(block));
    new_block->content = content;
    new_block->content_len = len;
    new_block->hash = hashb(content, len);
    printf("Title > ");
    read(0, &new_block->title[0], sizeof(new_block->title));

    if (blockchain == NULL) {
        blockchain = new_block;
    }
    else {
        block* cur = blockchain;
        for (; cur->next != nullptr; cur = cur->next);
        cur->next = new_block;
    }
    printf("[+] Block added, hash = %zu\n", new_block->hash);
}

void rmv() {
    if (blockchain == NULL) {
        puts("[!] No blockchain");
        return;
    }

    auto hash = read_hash();

    block* cur = blockchain;
    block* prev = NULL;
    for (; cur != nullptr && cur->hash != hash; cur = cur->next) {
        prev = cur;
    }
    
    if (!cur) {
        puts("[!] Block not found!");
        return;
    }

    if (!prev) {
        blockchain = cur->next;
    } else {
        prev->next = cur->next;
    }
    free(cur->content);
    memset(cur, 0, sizeof(*cur)); // secoority
    free(cur);

    puts("[+] Block rmved");
}

void view() {
    if (blockchain == NULL) {
        puts("[!] No blockchain");
        return;
    }

    auto hash = read_hash();

    block* cur = blockchain;
    for (; cur != nullptr && cur->hash != hash; cur = cur->next);
    
    if (!cur) {
        puts("[!] Block not found!");
        return;
    }

    printf("[*] Block found, hash = %zu\n", cur->hash);
    printf("Title: %s\n", cur->title);
    printf("Content:\n");
    write(1, cur->content, cur->content_len);
}

void edit() {
    if (blockchain == NULL) {
        puts("[!] No blockchain");
        return;
    }

    auto hash = read_hash();

    block* cur = blockchain;
    for (; cur != nullptr && cur->hash != hash; cur = cur->next);
    
    if (!cur) {
        puts("[!] Block not found!");
        return;
    }

    size_t len;
    auto content = read_content(&len);
    auto new_hash = hashb(content, len);

    printf("Title > ");
    read(0, &cur->title[0], sizeof(cur->title));

    if (new_hash != cur->hash) {
        puts("[!] Block hash mismatch!");
        free(content);
    } else {
        puts("[+] Block edited");
        free(cur->content);
        cur->content = content;
    }
}

int main() {
    setup();
    puts("[*] Web3 Blockchain AI Augmented Reality Portal with Ethereum and Shor's Algorithm for Maximum Encryption");
    puts("[>] TODO make the above a reality before our ICO. For now, investors can use the command line");
    puts("[>] There are no bugs in our super secure software, of course!");
    while(1) {
        menu();
        int opt;
        scanf("%d", &opt);
        switch (opt) {
            case 1: // add
                add();
                break;
            case 2: // rmv
                rmv();
                break;
            case 3: // view
                view();
                break;
            case 4: // edit
                edit();
                break;
            default:
                exit(1);
                break;
        }
    }
}