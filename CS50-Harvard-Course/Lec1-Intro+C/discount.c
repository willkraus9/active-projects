#include <cs50.h>
#include <stdio.h>

float discount(float price, int percentage);

int main(void)
{
    float regular = get_float("Regular Price: ");
    int percentage = get_int("Percent Off (as two numbers): ");
    float sale = discount(regular, percentage);
    printf("Sale Price: %.2f\n",sale);
}

float discount(float price, int percentage)
{
    return price * (100 - percentage)/100;
}
