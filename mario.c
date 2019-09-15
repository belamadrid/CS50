#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //make height n
    int n;
    do 
    //gets user to input height
    { 
        n= get_int("Height: ");
    }
    while (n < 1 || n > 8);
    
    for(int i=0; i < n; i++)
    {
        //prints number of spaces before #
        for(int k=n-(i +1); k>0; k--)
        {
            printf(" ");
        }
        //prints number of #
        for(int j=0; j < i+1; j++)
        {
            printf("#");  
        }
        printf("\n");
    }
}



    
