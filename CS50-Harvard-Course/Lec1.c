#include <stdio.h>
#include "cs50.h"

int main(void)

{
    string answer = get_string("What's Your Name?");
    printf("Hi there, %s!",answer);
}