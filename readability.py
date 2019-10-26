import cs50

#start letters and sentences at 0

letters = 0
sentences = 0

#words start at 1
words = 1

#get input
s = input("Write down your text: \n")

#counts letters in string
for i in range(len(s)):
    if s[i].isalpha():
        letters+=1


#counts number of words in a string
for i in range(len(s)):
   if s[i].isspace():
       words+=1

#counts number of sentences in a string
for i in range(len(s)):
   if s[i] == '.' or s[i] == '?' or s[i] == '!':
       sentences+=1

L = 100 * letters / words
S = 100 * sentences / words
index = round(0.0588 * L - 0.296 * S - 15.8)

#printing grade depending on index
if index >= 16:
    print("Grade 16+")

elif index < 1:
    print("Before Grade 1")

else:
    print(f"Grade {index}")




