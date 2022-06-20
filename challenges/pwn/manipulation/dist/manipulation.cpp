#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <cstdarg>
#include <vector>
#include <unistd.h>

using namespace std;

#define NAME_SZ 0x8

struct logger {
    FILE* inner;

    logger(const char*  path) {
        inner = fopen(path, "a");
    }

    void write(const char* pre, const char* fmt, va_list args) {
        char buf[512];
        snprintf(buf, sizeof(buf), pre, fmt);
        vfprintf(inner, buf, args);
    }

    void info(const char* fmt...) {
        va_list args;
        va_start(args, fmt);
        write("[*] %s\n", fmt, args);
        va_end(args);
    }

    void fatal(const char* fmt...) {
        va_list args;
        va_start(args, fmt);
        write("[!] %s\n", fmt, args);
        va_end(args);
        exit(1);
    }

    ~logger() {
        fclose(inner);
    }
};

struct account {
    double balance;
    char name[NAME_SZ];
};

account* accounts;
uint account_len;

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void menu() {
    puts("1. add more accounts");
    puts("2. set name");
    puts("3. tfr $");
    puts("4. print info");
}

void tfr(logger log, uint from, uint to, double amt) {
    if (from >= account_len || to >= account_len) 
        log.fatal("invalid transfer from %u -> %u, $%lf", from, to, amt);
    accounts[from].balance  -= amt;
    accounts[to].balance    += amt;
    log.info("transfer from %u -> %u, $%lf", from, to, amt);
}

uint read_num(const char* prompt) {
    printf("%s > ", prompt);
    uint n;
    scanf("%u", &n);
    return n;
}

double read_dbl(const char* prompt) {
    printf("%s > ", prompt);
    double n;
    scanf("%lf", &n);
    return n;
}

int main() {
    setup();
    auto log = logger("/tmp/log.txt");
    log.info("bank service launched @ %lld!", time(NULL));
    puts("Welcome to the Manipulation Bank App!");
    puts("How many accounts you want to create today?");
    account_len = read_num("Account Size");
    accounts = (account*) malloc(account_len * sizeof(account));
    
    while (1) {
        menu();
        int opt = read_num("opt");
        switch (opt) {
            case 1: // add more accounts
            {
                auto new_account_len = read_num("New Size");
                if (new_account_len < account_len)
                    log.fatal("attempt to make accounts smaller, %u->%u", account_len, new_account_len);

                auto new_accounts = (account*) malloc(new_account_len * sizeof(account));
                memcpy(new_accounts, accounts, account_len * sizeof(account));
                free(accounts);
                accounts = new_accounts;
                account_len = new_account_len;
                break;
            }
            case 2: // set name
            {
                auto idx = read_num("Account");
                if (idx >= account_len)
                    log.fatal("invalid account id %u", idx);

                printf("Name: ");
                read(0, accounts[idx].name, NAME_SZ);
                break;
            }
            case 3: // tfr $
            {
                auto from = read_num("From");
                auto to = read_num("To");
                auto amt = read_dbl("Amount");
                tfr(log, from, to, amt);
                break;
            }
            case 4: // print info
            {
                for (auto i = 0; i < account_len; i++) {
                    printf("%d. %s: %6.18e\n", i, accounts[i].name, accounts[i].balance);
                }
                break;
            }
            default:
                return 0;
                break;
        }

    }
}