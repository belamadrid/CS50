from cs50 import SQL
import sys

if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    exit()

house_name = sys.argv[1]

# access table
db = SQL("sqlite:///students.db")


# get names in house
people = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", house_name)

# print all names
for row in people:
    print(row["first"], end=" ")
    if row["middle"] != None:
        print(row["middle"], end=" ")
    print(row["last"], end=", born ")
    print(row["birth"])

