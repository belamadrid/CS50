#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

//start program by representing command line argument count and array of strings representing each argument
int main(int argc, string argv[])
{
    int i;
    int n;

//checks if argument count is not equal to 2
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

//https://stackoverflow.com/questions/29248585/c-checking-command-line-argument-is-integer-or-not
//so that goes through each i in the string in order to tell if it is a nondigit
    for (i = 0; i<strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 2;
        }
    }


 //define key as integer
    int k = atoi(argv[1]);


    string s= get_string("plaintext:  ");

    printf("ciphertext: ");

//goes through each part of string
    for (i = 0; i<strlen(s); i++)
    {
        //prints non alphabetical characters as plaintext
        if(!isalpha(s[i]))
        {
            printf("%c", s[i]);
        }


        //prints upper case alphabetical characters through ciphertext
        if (isalpha(s[i]) && isupper(s[i]))
        {
            printf("%c", (((s[i] - 65)+k)%26)+65);

        }

        //prints lower case alphabetical characters through ciphertext
        if (isalpha(s[i]) && islower(s[i]))
        {
            printf("%c", (((s[i] - 97)+k)%26)+97);

        }
    }

    printf("\n");



}