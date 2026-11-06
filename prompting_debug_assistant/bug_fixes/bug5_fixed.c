#include <stdio.h>

int main(void) {
    char name[8];
    const char *input = "Alexander";

    snprintf(name, sizeof name, "%.*s",
             (int)sizeof name - 1, input);

    printf("Name: %s\n", name);

    puts("bug5_fixed.c: test completed");
    return 0;
}
