
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






")



# Level 2
## User story 2
### "As a user, I want to be able to guess a number and know if I need to go higher or lower"

# while counter < 5:
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess < magic_number:
#         counter += 1
#         print("You guessed too low")
#     elif guess > magic_number:
#         counter += 1
#         print("You guessed too high")
#     else:
#         print("You guessed the magic number!")
#         break
# else:
#     print(f"You did not guess the magic number. It was {magic_number}.")


# Level 2
## User story 3
### As a user, I don't want my guesses wasted if I enter something accidentally as my guess
### which are not digits.

# while counter < 5:
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess < magic_number:
#         counter += 1
#         print("You guessed too low")
#     elif guess > magic_number:
#         counter += 1
#         print("You guessed too high")
#     else:
#         print("You guessed the magic number!")
#         break
# else:
#     print(f"You did not guess the magic number. It was {magic_number}.")


# Level 2
## User story 4
### As a user, after each guess, I would like to know how many guesses I have left.


while counter < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < magic_number:
        counter += 1
        print(f"You guessed too low, you now have {5 - counter} guesses remaining...")
    elif guess > magic_number:
        counter += 1
        print(f"You guessed too high, you now have {5 - counter} guesses remaining...")
    else:
        print("You guessed the magic number!")
        break
else:
    print(f"You did not guess the magic number. It was {magic_number}.")


# Level 3
## User story 5
### As a user, I would like the magic number to be randomly generated each time
### I play so it is more fun.

#### ====> already done using the random.randint() module and method.


## User story 6
### As a user, I would like to know the magic number at the end of the game if I still haven't
### guessed correctly and I've used up all my tries.


