import cs50
#get input and convert to coin
while True:
    try:
        n = float(input("Change owed: "))
    #https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
    #used ValueError as method to check if input is valid and if it wasn't to continue loop
    except ValueError:
        continue
    #if n is negative, continue loop
    if n < 0:
        continue
    #if float and nonnegative, break loop
    else:
        break

coins = round(n * 100)


#make sure that the number of coins start at 0

coinnumber = 0


#first check how many quarters can fit in the amount of change

while coins >= 25:
    #subtract quarter from coin total
    coins = coins - 25
    coinnumber += 1

#check dimes
while coins >= 10:
    coins = coins - 10
    coinnumber +=1

#check nickles

while coins >= 5:
    coins = coins -5
    coinnumber +=1

#check pennies
while coins >= 1:
    coins=coins - 1
    coinnumber += 1

#print the minimum number of coins

print(f"Coins needed: {coinnumber}")
