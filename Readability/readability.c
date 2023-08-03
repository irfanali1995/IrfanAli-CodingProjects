#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


int count_letters(char *s);
int count_spaces(char *s);
int count_punc(char *s);

int main(void)
{
// 0. getting user to type string
    string text = get_string("Text: ");


    int Letters = count_letters(text); // 1. calculate letters
    int words = count_spaces(text); // 2. count words separated by spaces
    int punc = count_punc(text); // 3. count sentence . , ! , ?

    float L = ((float)Letters / (float)words) * 100; //converting numbeber to float
    float S = ((float)punc / (float)words) * 100;


    float index = 0.0588 * L - 0.296 * S - 15.8;
    int round_result = round(index); //rounding off number to the nearest integer

    if (round_result < 1)
    {
        printf("Before Grade 1\n");
    }
    if (round_result >= 1 && round_result <= 16)
    {
        printf("Grade %i\n", round_result);
    }

    if (round_result > 16)
    {
        printf(" Grade 16+\n");
    }


}




// Function to count the letters in string
int count_letters(char *s)
{
    int l = 0;
    int length = strlen(s);
    for (int i = 0; i < length ; i++)
    {

        if (isalpha(s[i]))
        {
            l++;
        }
    }

    return l;

}


// Function to count the words in string
int count_spaces(char *s)
{
    int w = 1; //There is no space after the last word
    int length = strlen(s);
    for (int j = 0; j < length ; j++)
    {
        if (isspace(s[j]))
        {
            w++;
        }

    }
    return w;
}


// Function to count the sentence in string by counting '.' , '?' , '!'
int count_punc(char *s)
{
    int p = 0;
    int length = strlen(s);
    for (int k = 0; k < length; k++)

    {
        if (s[k] == '?' || s[k] == '.' || s[k] == '!')
        {
            p++;
        }
    }
    return p;
}
