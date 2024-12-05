
# Level 1
import random

magic_number = random.randint(0,11)
counter = 0


while counter < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != magic_number:
        counter += 1
    else:
        print("You guessed the magic number!")
        break
else:
    print(f"You did not guess the magic number. It was {magic_number}.")






