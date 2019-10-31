Week 6 Notes

PYTHON

hello.py

PRINTING IN C
print("hello, world")

PRINTING INPUT
answer = get_string("What's your name?\n")
print("hello, " + answer) or print("hello,", answer) OR print(f"hello, {answer}") (f turns into format string)

MAKE VARIABLE (don't have to define as int)

counter = 0

counter = counter +1 OR counter+=1

IF STATEMENTS
if x < y:
    print("x is less than y")

if x < y:
    print("x is less than y")
else:
    print("x is not less than y")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


WHILE STATEMENTS
while True:
    print("hello, world")


i = 3
while i > 0:
    print("cough")
    i -= 1

FOR LOOPS
//while i goes through 0,1,2
for i in [0, 1, 2]:
    print("cough")

aka

for i in range(3):
    print("cough")

TERMS

range (sequence of numbers)
list (sequence of mutible values (like array that can b inc))
tuple (sequence of inmutible values, like gps coordinates)
dict (collection of key value pairs)
set (collection of unique values)


dictionary.py

def check(word):
    if word in words:
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()
    return True

def size():
    return len(words)

def unload():
    return True

EXAMPLES

if s == "Y" or s =="y":
    print("Agreed.")
aka
if s in ["Y", "y"]:
    print("Agreed.")

aka
if s.lower() in ["y"]:
    print("Agreed.")


def main():
    for i in range(3):
        cough()

def cough():
    print("cough")

main()

print("cough\n" *3)


while True:
    n= get_int("positive integer:")
    if n>0:
        break
return n (n is accessible outside indentations but not outside function)


mario

for i in range(4):
    print("?", end="")
print()

print("#\n" *3, end = "")

for i in range(3):
    for j in range(3):
        print("#", end ="")
    print()

INPUT INSTEAD OF get_string
s = input("What's your name?\n")

age = int(input("What's your age?\n"))

i= 1
while True:
    print(i)
    //waits second before printing next 1
    sleep(1)
    i*=2

//make array of scores
scores = []
//adding something to the array
scores.append(72)
scores.append(73)

//iterating over characters of string

s = get_string("Input: ")
print("Output: ", end = "")
for i in range(len(s)):
    print(s[i], end="")
print()

aka
s = get_string("Input: ")
print("Output: ", end = "")
for c in s:
    print(c, end="")
print()


from sys import argv

for i in range(len(argv)):
    print(argv[i])

aka
for arg in argv:
    print argv

if len(argv) != 2:
    print("missing command-line argument")
    exit(1)
print(f"hello, {argv[1]}")

people={
    "EMMA": "5555555555",
    "RODRIGO": "7777777777"
}

if "EMMA" in people:
    print(f"Found {people['EMMA']}")

COMPARE TWO STRINGS
s= get_string("s: ")
t= get_string("t: ")

if s==t:
    print("same")
else:
    print("different")


s= get_string("s: ")
t=s
t=t.capitalize()

print(f"s: {s}")
print(f"t: {t}")

x=1
y=2
print(f"x is {x}, y is {y}")
x, y = y, x
print(f"x is {x}, y is {y}")

ADD NUMBERS TO PHONEBOOK
file open("phonebook.csv", "a")
name=get_string("Name: ")
number= get_string("Number: ")
writer=csv.writer(file)
writer.writerow(name, number)
file.close()

aka
file open("phonebook.csv", "a")
name=get_string("Name: ")
number= get_string("Number: ")
with open
writer=csv.writer(file)
writer.writerow(name, number)
file.close()


#SECTION

import not #include

no longer need to include variable type

#print non string
print(str(someNonString))

#To concatenate multiple strings
priint(strOne + strTwo + strThree)

#format variables for printing this way
print( f"someText {someVariable}")

#RUNNING
#no need to make
python filename.py

#arrays/lists

#create: place values in square brackets [], separated with commons
myList= [12,0,13]

#add element to end of list
myList.append(10)

#remove element from a list
myList.remove(13)

#to make a real copy
myList.copy()

#sort
myList.sort()

#Tuples are immutable

#Dictionaries are ways to make lists of data that we can access with key word
myDictionary = {"Yale": "New Haven", "Harvard": "Cambridge"}

#Num values in dic
len(myDictionary)

#FUNCTIONS



