#!/usr/bin/env python3

lower_day = 1
upper_day = 31
lower_month = 1
upper_month = 12
lower_year = 2000
upper_year = 2021

my_birthday_year = 2000
my_birthday_mon = 7
my_birthday_day = 28

count=0
guess=0

while count < 10:
    count += 1
    # taking guessing number as input
    raw_guess = input("Guess my birth month:- ")

    if raw_guess.isnumeric():
        pass
    else:
        print("Please provide a numeric value")
        continue

    guess = int(raw_guess)
    # Condition testing
    if my_birthday_mon == guess:
        print("Congratulations, you got the month right in",count, " tries")
        break
    elif guess <= lower_month or guess > upper_month:
        print("Please provide valid months")
    elif my_birthday_mon > guess:
        print("You guessed month too small!")
    elif my_birthday_mon < guess:
        print("You Guessed month too high!")

if count >= 10:
    print("\tBetter Luck Next time!")
    print("\nThe birth month is %d" % my_birthday_mon)

count = 0
guess = 0

while count < 10 and my_birthday_day != guess:
    count += 1
    ## taking guessing number as input
    raw_guess = input("Guess my birth day:- ")
    try:
       guess =  int(raw_guess)
    except ValueError:
        print("Please enter numeric value")
        continue

    # Condition testing
    if my_birthday_day == guess:
        print("Congratulations, you got the day right in",count, " tries")
    elif guess <= lower_day or guess > upper_day:
        print("Please provide a valid value")
    elif my_birthday_day > guess:
        print("You guessed day too small!")
    elif my_birthday_day < guess:
        print("You Guessed day too high!")

if count >= 10:
    print("\tBetter Luck Next time!")
    print("\nThe birth day is {my_birthday_day}")

count = 0
guess = 0
while count < 10:
    count += 1
    # taking guessing number as input
    raw_guess = input("Guess my birth year between 2000 and 2020:")
    try:
        guess = int(raw_guess)
    except ValueError:
        print("Please provide a numeric value")

    # Condition testing
    if my_birthday_year == guess:
        print("Congratulations, you got the year right",count, " tries")
        break
    elif guess< lower_year or guess > upper_year:
        print("Please provide value between 2000 and 2021")
    elif my_birthday_year > guess:
        print("You guessed the year too small!")
    elif my_birthday_year < guess:
        print("You Guessed the year too high!")

if count >= 10:
    print("\tBetter Luck Next time!")
    print("\nThe birth year is %d" % my_birthday_year)

print (f"My birthday is {my_birthday_mon} / {my_birthday_day} / {my_birthday_year}")


