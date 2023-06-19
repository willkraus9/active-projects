//#include <cs50.h>
#include <stdio.h>

int main(void)
 {
    int number_scores = get_int("How many scores?");
    int scores[number_scores];
    for (int i = 0; i < number_scores; i++)
        {
            scores[i] = get_int("Score: ");
        }
    printf("Average: %f\n", ((scores[0] + scores[1] + scores[2]) / 3.0));
  
 }
