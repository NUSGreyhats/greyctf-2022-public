#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>

#include "hash.h"

bool auth(const char* msg, unsigned long h, size_t len) {
    return hash(msg, len) == h;
}

void sendMessage(const char *msg) {
    printf("0x%016lx:%s\n", hash(msg, strlen(msg)), msg);
}

char* getMessage(char *buf) {
    read(0, buf, 100);

    char *sTag = strtok(buf, ":");
    char *sMsg = strtok(NULL, ":");

    if (sTag == NULL || sMsg == NULL) {
        puts("Corrupted message");
        exit(1);
    }

    unsigned long tag = strtol(sTag, NULL, 16);

    sMsg[strcspn(sMsg, "\n")] = '\0';

    if (!auth(sMsg, tag, strlen(sMsg))) {
        puts("Corrupted message");
        exit(1);
    }

    char *msg = malloc(strlen(sMsg));
    memcpy(msg, sMsg, strlen(sMsg));
    return msg;
}

int main (int argc, char **argv) {
    setvbuf(stdout, NULL, _IONBF, 0);
    const char *flag = getenv("FLAG");
    const char *adminPass = getenv("PASS");
    // const char adminPass[] = "THIS_IS_FINE";
    const char adminUser[] = "administrator";

    if ( hash(adminPass, strlen(adminPass)) != 0x3dd99b6c9d29c576) {
        puts("System failed, check with support");
        exit(1);
    }

    // // This is only for challenge generation
    //    sendMessage(adminUser);
    //    sendMessage(adminPass);

    char buf[100];
    sendMessage("Welcome to MBA management system");
    sendMessage("Login:");
    char *user = getMessage(buf);
    sendMessage("Password:");
    char *password = getMessage(buf);

    unsigned long h = hash(password, strlen(password));
    unsigned long expectedH = hash(adminPass, strlen(adminPass));

    if (!strcmp(user, adminUser) && h == expectedH) {
        puts(flag);
        free(user);
        free(password);
        return 0;
    } else {
        puts("Auth failed");
        free(password);
        free(user);
    }

}