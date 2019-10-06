#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

   for (int i=0; i< height; i++)
   {
       for(int j=0; j< width; j++)
       {
           int average =round( (float)(image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen)/3);
           image[i][j].rgbtRed = average;
           image[i][j].rgbtBlue = average;
           image[i][j].rgbtGreen = average;

       }
   }
   return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i=0; i< height; i++)
   {
       for(int j=0; j<width; j++)
       {
           int sepiaRed = round( .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
           int sepiaGreen = round( .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
           int sepiaBlue = round ( .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

           if (sepiaRed >255)
           {
               sepiaRed=255;
           }

           if (sepiaGreen >255)
           {
               sepiaGreen=255;
           }

           if (sepiaBlue >255)
           {
               sepiaBlue=255;
           }
            image[i][j].rgbtRed =sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue=sepiaBlue;

       }
   }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
   for (int i=0; i< height; i++)
   {
       for(int j=0; j<width/2; j++)
       {
           RGBTRIPLE a= image[i][j];
           image[i][j]=image[i][width - 1 - j];
           image[i][width - 1 - j] = a;
       }
   }



    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0; i< height; i++)
   {
       for(int j=0; j<width; j++)
       {
          int sumR=0;
          int sumB=0;
          int sumG=0;
          int numPixels=0;
          RGBTRIPLE a[height][width];
          for (int k=i-1; k< i+1; k++)
          {
              for (int l=j-1; l< j+1; l++)
              {
                  if (0<l && 0<k && l<width && k<height)
                  {
                      sumR += image[k][l].rgbtRed;
                      sumG += image[k][l].rgbtGreen;
                      sumB += image[k][l].rgbtBlue;
                      numPixels++;

                  }

                  int avgR= round(sumR/(numPixels * 1.0));
                  int avgG= round(sumG/(numPixels*1.0));
                  int avgB= round(sumB/(numPixels*1.0));

                  a[i][j].rgbtRed= avgR;
                  a[i][j].rgbtGreen= avgG;
                  a[i][j].rgbtBlue= avgB;
                  image[i][j].rgbtRed= a[i][j].rgbtRed;
                  image[i][j].rgbtGreen= a[i][j].rgbtGreen;
                  image[i][j].rgbtBlue= a[i][j].rgbtBlue;
              }
          }

       }
   }
   return;
}


/*
               float redsurrounds= image[k][l].rgbtRed ;
               float bluesurrounds= image[k][l].rgbtBlue;
               image[k][l].rgbtGreen = float greensurrounds;
              }
          }





           int redaverage =round( (float)(image[i-1][j-1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed + image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i][j+1].rgbtRed + image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed)/9);
           int blueaverage =round( (float)(image[i-1][j-1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue + image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue + image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue)/9);
           int greenaverage =round( (float)(image[i-1][j-1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen + image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen + image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen)/9);
           image[i][j].rgbtRed = redaverage;
           image[i][j].rgbtBlue = blueaverage;
           image[i][j].rgbtGreen = greenaverage;
       }

   }
    return;
}
*/