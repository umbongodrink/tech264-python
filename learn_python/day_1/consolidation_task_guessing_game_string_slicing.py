
original_word = "recommendation"
scrambled_word = "eoommandretnic"


hint1_slice = original_word[4:6]
#print(hint1_slice)
hint2_slice = original_word[-3:]
#print(hint2_slice)
hint3_slice = original_word[7:10]
#print(hint3_slice)
hint4_slice = original_word[0:2]
#print(hint4_slice)


print("Scrambled word: ", scrambled_word)
print("Guess the original word from the scrambled version.")
print("Here are some hints:")

print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")
print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")
print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")
print("Hint 4: The first two letters are '" + hint4_slice + "'.")

print("What's your guess?")