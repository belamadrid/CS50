// Implements a dictionary's functionality

#include <stdbool.h>

#include "dictionary.h"

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
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int start = tolower(word[0]) - 'a';
    //then what do you return?
    return 0;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)

{
    //initialize hash table (set each bucket to null)
    for (int i =0, i<table[i], i++)
    {
        //set hash table buckets to null
        table[i]=NULL
    }

    // attempt to open our file
    file *dictionary = fopen("dictionary", "r")
    if (dictionary == NULL)
    {
        return false;
    }
    //iterate thru file one word at a time
    //fscanf
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    return false;
}
