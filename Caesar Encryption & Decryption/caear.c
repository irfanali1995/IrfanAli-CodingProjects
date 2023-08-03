#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument

    if (argc != 2)
    {
        printf("Usage: %s <number>\n", argv[0]);
        return 1; // Return non-zero value to indicate an error
    }

    // Make sure every character in argv[1] is a digit
    char *String = argv[1];
    for (int i = 0; String[i] != '\0'; i++)
    {
        if (!isdigit(String[i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert argv[1] from a string to an integer
    int number = atoi(String);

    // Prompt user for plaintext
    char plaintext[1000];
    printf("plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);

    // For each character in the plaintext:
    printf("ciphertext: ");
    // Rotate the character if it's a letter
    for (int i = 0; plaintext[i] != '\0'; i++)
    {
        char ch = plaintext[i];

        if (isalpha(ch))
        {
            char base = isupper(ch) ? 'A' : 'a';
            char rotated = ((ch - base + number) % 26) + base;
            putchar(rotated);
        }

        else
        {
            putchar(ch);
        }
    }
    printf("\n");

    return 0; // Return 0 to indicate successful execution
}
