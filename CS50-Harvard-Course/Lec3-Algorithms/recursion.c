#include <cs50.h>
#include <stdio.h>

void draw (int n);

int main (void)
{
    int height  = get_int("Height: ");
    draw(height);

}
void draw (int n)
{
   if (n<=0) // no negative numbers
   {
       return;
       //stop drawing when get 1 brick

   }
    draw (n-1);
    for (int i = 0; i<n; i++)
    {
        printf("#");
    }
    printf("\n");
    //draw bricks (#) for n lines 
}
