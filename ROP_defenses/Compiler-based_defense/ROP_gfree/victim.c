#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void helper() {
    //"pop %rdi; pop %rsi; pop %rdx; ret"
    char cheat[] = "\x5f\x5e\x5a\xc3";
}

void vulnerable_function() {
    char buf[128];
    read(0, buf, 256);
}

int main() {
    vulnerable_function();
    write(1, "Hello, World\n", 13);
}
