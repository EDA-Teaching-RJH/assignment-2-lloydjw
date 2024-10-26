### Part Two -- your code goes here. 
import random

correct = False
guessed = []
answer = random.randint(1,100)
while correct == False:
    guess = int(input("guess a number between 1 and 100: "))
    if guess <= 100 and guess >= 1:
        if guess == answer:
            print("you guessed",answer,"correctly")
            correct = True
        elif guess in guessed:
            print("you have already guessed",guess)
        else:
            print("try again")
            guessed.append(guess)
    else:
        print("number must be between 1 and 100 please")