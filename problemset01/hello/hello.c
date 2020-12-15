/**
|-------------------------------------------------------------------------------
| hello.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jun 29, 2020
| Compilation:  make hello
| Execution:    ./hello
|
| This program displays a simple greeting to the user.
|
*/

#include <stdio.h>

int main(void)
{
    char name[100];

    printf("What is your name?\n");
    scanf("%s", name);
    printf("hello, %s\n", name);
}
