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
           RGBTRIPLE pixel = image[i][j];
           int average = ((pixel.rgbtRed + pixel.rgbtBlue + pixel.rgbtGreen)/3);
           pixel.rgbtRed = average;
           pixel.rgbtBlue = average;
           pixel.rgbtGreen = average;

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
           RGBTRIPLE pixel = image[i][j];
           float sepiaRed = .393 * pixel.rgbtRed + .769 * pixel.rgbtGreen + .189 * pixel.rgbtBlue;
           float sepiaGreen = .349 * pixel.rgbtRed + .686 * pixel.rgbtGreen + .168 * pixel.rgbtBlue;
           float sepiaBlue = .272 * pixel.rgbtRed + .534 * pixel.rgbtGreen + .131 * pixel.rgbtBlue;
           sepiaRed= round (sepiaRed);
           sepiaGreen= round (sepiaGreen);
           sepiaBlue= round(sepiaBlue);
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
