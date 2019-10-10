// Implements a dictionary's functionality

#include <stdbool.h>

#include "dictionary.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);
    node *cursor = table[index];
    //access linked list at index in hash table
    while (cursor != NULL)
    {
        if (strcasecmp(cursor -> word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }


    return false;
}

// Hashes word to a number
/* unsigned int hash(const char *word)

    int start = tolower(word[0]) - 'a';
    //then what do you return?
    return 0;
*/

#define MULTIPLIER (37)
unsigned int hash(const char *s)
{

    unsigned long h;
    unsigned const char *us;

    // cast s to unsigned const char
    // this ensures that elements of s will be treated as having values >= 0
    us = (unsigned const char *) s;

    h = 0;
    while(*us != '\0')
    {
        h = h * MULTIPLIER + *us;
        us++;
    }

    return h;


}


unsigned int wordcount = 0;
// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)

{
/*
    //initialize hash table (set each bucket to null)
    for (int i = 0; i <= 25; i++)
    {
        //set hash table buckets to null
        table[i] = NULL;
    }
*/

    // attempt to open our file
    FILE *dictionaryfile = fopen(dictionary, "r");
    //if doesn't open
    if (dictionaryfile == NULL)
    {
        return false;
    }

    //iterate thru file one word at a time
    //fscanf
    char wordd[LENGTH + 1];
    while (fscanf(dictionaryfile, "%s", wordd) != EOF)
    {
        int h = hash(wordd);
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            return false;
        }

        strcpy(newNode -> word, wordd);
        wordcount++;
        newNode -> next = table[h];
        table[h] = newNode;

    }
    fclose(dictionaryfile);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return wordcount;
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{

    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *placeholder = cursor;
            cursor = cursor -> next;
            free(placeholder);

        }
    }


    return true;
}
