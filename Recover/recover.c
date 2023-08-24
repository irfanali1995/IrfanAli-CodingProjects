#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n"); // Checking correct usage in command-line
        return 1;
    }

    FILE *inptr; // creating file pointer

    inptr = fopen(argv[1], "r"); // opening file provided in argument

    if (inptr == NULL) // checking if file is NULL
    {
        printf("Error opening file"); 
    }

    unsigned char buffer[511]; // creating a buffer size of 512
    FILE *outptr = NULL;       // creating file pointer for output
    int jpeg_counter = 0;      // initating jpeg_counter

    while (fread(buffer, 1, 512, inptr))
    {
        char filename[8]; // creating filename
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {

            if (outptr != NULL) // checking if outptr is not NULL
            {
                fclose(outptr);
            }

            sprintf(filename, "%03i.jpg", jpeg_counter); // creating a file name ###.jpg
            jpeg_counter++;

            outptr = fopen(filename, "wb"); // writing new file in binary

            if (outptr == NULL) // if memory is null , return error
            {
                fprintf(stderr, "Could not create %s\n", filename);
                return 2;
            }
        }

        if (outptr != NULL) // writing file if it's not null
        {
            fwrite(buffer, 1, 512, outptr);
        }
    }

    // Close any open files
    if (outptr != NULL)
    {
        fclose(outptr);
    }

    fclose(inptr);
}
