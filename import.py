import csv
import sys
from cs50 import SQL

# walkthrough with Reese on Nov. 3

# read in file
if len(sys.argv) != 2:
    exit()

file_name = sys.argv[1]
file = open(file_name, "r")
people = csv.DictReader(file)


db = SQL("sqlite:///students.db")


# determine format of each name
for row in people:
    house = row["house"]
    birth = row["birth"]
    name_list = row["name"].split()
    if len(name_list) == 2:
        # takes first element and set it to first, takes last and set it to last
        first, last = name_list
        middle = None
    else:
        first, middle, last = name_list

# add to table
# insert into students and give values to fill in
    db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?,?,?,?,?)", first, middle, last, house, birth)