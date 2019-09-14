#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // prints a statement to the screen
    printf("hello, world\n");
    // gets user name input and prints it out 
    string name = get_string("What is your name?\n");
    printf("hello, %s\n", name);
}


