#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//went through walkthrough in office hours 10/6
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return 1;
    }

    //open memory card
    FILE *file = fopen(argv[1], "r");
    //check if file does not exist
    if (file == NULL)
    {
        printf("File did not open");
    }
    //declare buffer
    unsigned char buff[512];
    //start jpgnumber count at 0
    int jpgnum = 0;
    char filename[8];
    FILE *outfile;
    //while block size is 512
    while (fread(buff, 1, 512, file) == 512)
    {
        //make sure file format is a jpeg by checking first four bytes
        if (buff[0] == 0xff && buff[1] == 0xd8 && buff[2] == 0xff && (buff[3] & 0xf0) == 0xe0)
        {
            //close file
            if (jpgnum > 0)
            {
                fclose(outfile);
            }
            //set jpg number count
            sprintf(filename, "%03i.jpg", jpgnum);
            jpgnum++;
            outfile = fopen(filename, "w");
            fwrite(buff, 1, 512, outfile);

        }
        else
        {

            //in process of writing to existing jpg
            if (jpgnum != 0)
            {
                fwrite(buff, 1, 512, outfile);
            }
        }
    }


}
