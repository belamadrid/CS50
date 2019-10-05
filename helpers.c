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


       }
   }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
