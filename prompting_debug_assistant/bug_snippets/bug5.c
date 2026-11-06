#include <stdio.h>
#include <string.h>

/* Intended: copy a name into a fixed-size buffer and print it safely. */
int main(void) {
    char name[8];
    const char *input = "Alexander";

    /* BUG: input is longer than the destination buffer can hold. */
    strcpy(name, input);
    printf("Name: %s\\n", name);
    printf("Name length: %zu\\n", strlen(name));

    return 0;
}
