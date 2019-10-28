import cs50
import csv
import sys
from sys import argv, exit

#check if there are not 3 command line args
if len(argv) != 3:
    print("missing command-line argument")
    exit(1)
#open csv file and dna sequence
csv = csv.DictReader(open(sys.argv[1]))
dna = (open(sys.argv[2]).read())


subsequences = csv.fieldnames[1:]
#make dictionary
dictionary = {}

#walkthrough at OH on 10/27/19
#subsequence is the header row
for subsequence in subsequences:
    best = 0
    for j in range(len(dna)):
        counter = 0
        #window = sequences[j : j+len(subsequence)]
        while True:
            start = j + counter*len(subsequence)
            end = start + len(subsequence)
            #string of letters
            #if the dna sequence we scanned from the start to the end is equal to one of the subsequences
            if dna[start: end] == subsequence:
                counter += 1
            else:
                break
        #set new counter as best (most appearances of subsequence)
        if counter > best:
            best = counter
        #add bests into dictionary
        dictionary[subsequence] = best


for person in csv:
    match = True
    for subsequence in subsequences:
        # print(f"dictionary: {dictionary[subsequence]}")
        # print(f"person {int(person[subsequence])}")
        #if dictionary entries not equal to any in database, break, set match to false
        if dictionary[subsequence] != int(person[subsequence]):
            match = False
            break
    #if match is still equal to true, that means there is a real match!
    if match == True:
        print(person["name"])
        break

if match == False:
    print("No match")

















