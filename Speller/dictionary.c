// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choosing larger prime number for even distribution
const unsigned int N = 17671;

// Hash table
node *table[N];

// Word count
int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hash_value = hash(word);
    node *node_pointer = table[hash_value];

    while (node_pointer != NULL) // Loop continues until it reaches terminator or NULL
    {

        if (strcasecmp(node_pointer->word, word) == 0)
        {
            return true;
        }
        node_pointer = node_pointer->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word) // modified hash function with help of Duck Debugger
                                    // Source: Data Structures of Dr. Rob Edwards from San Diego State University
{
    // Improve this hash function
    int hash_value = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        char lowercase = tolower(word[i]); // Convert character to lowercase
        hash_value = (31 * hash_value + lowercase) % N;
    }

    return hash_value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        node *temp = malloc(sizeof(node));
        if (temp == NULL)
        {
            return false;
        }
        strcpy(temp->word, word);
        int index = hash(word);
        if (table[index] == NULL)
        {
            temp->next = NULL;
            table[index] = temp;
        }
        else
        {
            temp->next = table[index];
            table[index] = temp;
        }
        word_count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *temp = table[i];
        node *cursor = table[i];
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(temp);
            temp = cursor;
        }
    }
    return true;
}
