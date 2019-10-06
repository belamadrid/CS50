#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return 1;
    }

    //open memory card
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("File did not open");
    }
    //printf
    unsigned char buff[512];
    int jpgnum=0;
    char filename[8];
    FILE* outfile = fopen(filename ,"w");
    while (fread( buff, 1, 512, file) == 512)
    {
        if (buff[0]== 0xff && buff[1] == 0xd8 && buff[2] == 0xff)
        {
            if(jpgnum > 0)
            {
                fclose(outfile);
            }

            sprintf(filename, "%03i.jpg", jpgnum);
            jpgnum++;
            fwrite(buff, 1, 512, outfile);

        }
        else
        {

            //in process of writing to existing jpg
            if(jpgnum != 0)
            {
                fwrite(buff, 1, 512, outfile);
            }
        }
    }


}
