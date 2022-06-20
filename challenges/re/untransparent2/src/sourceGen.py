import sys



prefix = """
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    int idx=0; int score=0;
    srand(3133337);
    int target = rand()%1000;
    char flag[50];
    read(0, flag, 50);
"""


flag = sys.argv[1] 


def correctIf():
    ret = ""
    for i in range(len(flag)):
        ret += f"if (flag[idx] == '{flag[i]}') {{"
        ret += "\n score++; idx++;"
        ret += "\n}"

    return ret


body = ''

for i in range(1000):
    body += f"if (target == {i}) {{"
    # the expected value
    if i == 589:
        body += correctIf()
    else:
        body += '\nscore--;'

    body += "\n}"



suffix = f"if (score == {len(flag)}) {{"
suffix += '\nputs("The flag reveals itself");'
suffix += '\n} else {' 
suffix += '\nputs("You gaze into the abyss");'
suffix += '\n}'

suffix += """
return 0;
}
"""

with open("pain.c", "w") as f:
    f.write(prefix + body + suffix)

with open("flag.txt", "w") as f:
    f.write(flag)
