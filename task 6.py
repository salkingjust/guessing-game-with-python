import random

randomNumbers = random.randint(1, 100)
userChoice = 0
chances = 5

print("welcome to the number guessing game")
print(f"you have {chances} chances to guess the number between 1 to 100 ")
while userChoice != randomNumbers and chances > 0:
    userChoice = int(input(f"Guess the number in my mind({chances} chances left): "))
    if userChoice < randomNumbers:
        print("Your choice is too low!")

    elif userChoice > randomNumbers:
        print("Your choice is too high!")
    chances -= 1
if userChoice == randomNumbers:
    print(f"You've guessed correctly! The number was {randomNumbers}.")
else:
    print(f"Sorry, you have run out of chances. The number was {randomNumbers}. Better luck next time!")
