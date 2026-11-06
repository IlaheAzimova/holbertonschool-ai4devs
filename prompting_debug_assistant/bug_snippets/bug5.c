#include <stdio.h>
#include <string.h>

/* Intended: copy a name into a fixed-size buffer and print it safely. */
int main(void) {
    char name[8];
    const char *input = "Alexander";

    strcpy(name, input);
    printf("Name: %s\n", name);

    return 0;
}
