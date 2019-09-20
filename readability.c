#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)

{
    //define letter count, word count, sentence count, and index as integer
    int letters;
    letters=0;
    int words = 0;
    //start words at 1 because there is no space before the first word in the text
    words=1;
    int sentences;
    sentences=0;
    int i;
    int index;


    string s= get_string("Write down your text: \n");

    //i starts at 0 and goes up until text hits null terminator
    for (i=0; s[i] != '\0'; i++)
    {
        //ctype.h detects letters in string
        if (isalpha(s[i]))
        {
            letters++;
        }
    }

    for (i=0; s[i] != '\0'; i++)
    {
        //ctype.h detects spaces in string which can represent number of words if you start counting at 1
        if (isspace(s[i]))
        {
            words++;
        }
    }

    for (i=0; s[i] != '\0'; i++)
    {
        //detects sentence as number of . or ? or !
        if (s[i]=='.' || s[i]=='?' || s[i]=='!')
        {
            sentences++;
        }
    }

// Theo Lauriette showed me that I had to express L, S, letters, and words as floats because they were used to calculate the average
float L = 100 * (float) letters / (float) words;
float S = 100 * (float) sentences / (float) words;


index = round(0.0588 * L - 0.296 * S - 15.8);

if (index>=16)
{
    printf("Grade 16+ \n");
}

else if (index<1)

{
    printf("Before Grade 1 \n");
}
else
{
    printf("Grade %d \n", index);
}


}

