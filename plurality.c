#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{

    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
//check if vote string name exists
bool vote(string name)
{
    for (int j = 0; j < candidate_count; j++)
    {
        int result = strcmp(name, candidates[j].name);
        if (result == 0)
        {
            //update vote total
            candidates[j].votes++;
            return true;

        }

    }
    return false;
}

void print_winner(void)
{
//check for max
    int max = 0;
    for (int a = 0; a < candidate_count; a++)
    {
        if (candidates[a].votes > max)
        {
            max = candidates[a].votes;

        }

    }
//link candidate with max votes to max names and print value
//Claire Recamier informed me I should try to use "a second loop" in order to link max votes to name.
    for (int a = 0; a < candidate_count; a++)
    {
        if (candidates[a].votes == max)
        {
            printf("%s\n", candidates[a].name);

        }

    }


}





