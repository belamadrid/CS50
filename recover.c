#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

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
    FILE* outfile;
    while (fread( buff, 1, 512, file) == 512)
    {
        if (buff[0]== 0xff && buff[1] == 0xd8 && buff[2] == 0xff && (buff[3] & 0xf0) == 0xe0)
        {
            if(jpgnum > 0)
            {
                fclose(outfile);
            }

            sprintf(filename, "%03i.jpg", jpgnum);
            jpgnum++;
            outfile = fopen(filename ,"w");
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
