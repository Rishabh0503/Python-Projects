# # THE GUESSING GAME
import random

print("WELCOME TO THE GUESSING GAME !")

upper_range=input("ENTER THE UPPER RANGE: ")
if upper_range.isdigit():
    upper_range = int(upper_range)
else:
    print("PLEASE ENTER A DIGIT")
    exit()
lower_range=input("ENTER THE LOWER RANGE: ")
if lower_range.isdigit():
    lower_range = int(lower_range)
else:
    print("PLEASE ENTER A DIGIT")
    quit()

random_num = random.randint(lower_range,upper_range)

guesses=0
while True:
    guesses+=1
    guess=input("Make a guess! ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("ENTER A DIGIT")
        continue
    if guess == random_num:
        print("You Guessed It!")
        break
    elif guess > random_num:
        print("You are guessing high")
    else:
        print("You are guessing low")

print(f"YOU GUESSED THE NUMBER IN {guesses} GUESSES")
if guesses <= 5:
    print("EXCELLENT GUESSING !")
elif guesses >= 10:
    print("AVERAGE GUESSING !")
else:
    print("POOR GUESSING !")