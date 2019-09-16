#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
    
{
    //because n is not an integer
    float n;
    //integer for coins and coinnumber
    int coinnumber;
    int coins;
    do 
    {
        //get input and convert to coins 
        n = get_float("Change owed: ");
        coins = round(n * 100);  
    }
    //make sure n is above 0 and that the number of coins start at 0
    while (n <= 0);
    coinnumber = 0;
   
    //first check how many quarters can fit in the amount of change
    while (coins >= 25)
    {
        //subtract quarter from coin total
        coins = coins - 25;
        coinnumber ++;
    }

    //check dimes
    while (coins >= 10)
    {
        coins = coins - 10;
        coinnumber ++;
    }

    //check nickles
    while (coins >= 5)
    {
        coins = coins - 5;
        coinnumber ++;
    }

    //check pennies
    while (coins >= 1)
    {
        coins = coins - 1;
        coinnumber ++;
    }

    //print the minimum number of coins
    printf("%i\n", coinnumber);
  
}
