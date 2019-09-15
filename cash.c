#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
    
{
    float n;
    int coinnumber;
    int coins;
    do 
    {
        n = get_float("Change owed: ");
        coins = round(n*100);  
    }
    while (n <= 0);
    coinnumber = 0;
   
    
    while (coins >= 25)
    {
        coins= coins-25;
        coinnumber ++;
    }
    
    while (coins >= 10)
    {
        coins = coins-10;
        coinnumber ++;
    }
    
    while (coins >= 5)
    {
        coins = coins-5;
        coinnumber ++;
    }
    
    while (coins >= 1)
    {
        coins = coins-1;
        coinnumber ++;
    }
    
    printf("%i\n", coinnumber);
    
}
