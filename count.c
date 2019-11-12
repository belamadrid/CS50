#include <stdbool.h>
#include <stdio.h>

typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./count INPUT\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        printf("Could not open file.\n");
        return 1;
    }

    int c;
    int count = 0;
    for (c = 0; (c = fgetc(file)) != EOF; c++)
    {
        if ((c & 0xC0) != 0x80)
        {
            count++;
        }
    }
    printf("Number of characters: %i\n", count);
}