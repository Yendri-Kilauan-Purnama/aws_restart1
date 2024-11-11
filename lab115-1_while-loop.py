# Lab Nomor 8, Working with Loops
# chances, dikasih kesempatan sampai 3x 
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isGuessRight = False
#setting = input(nilai)
chances = 0 

while isGuessRight != True and chances <=3:
    guess = input("Guess a number between 1 and 10: ")
    # number = random.randint(1,10)
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        print("Selamat anda mendapatkan piala")
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        chances += 1
        

