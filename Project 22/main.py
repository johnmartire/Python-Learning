import random

# Word list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Placeholder list to represent guessed progress
display = ["_"] * word_length

# Set the number of attempts
attempts = 10

# Print the chosen word for testing purposes (remove in the actual game)
print(f"The chosen word is: ")

# Game loop with limited attempts
while "_" in display and attempts > 0:
    guess = input(f"Guess a letter ({attempts} attempts remaining): ").lower()
    
    # Deduct one attempt for each guess
    attempts -= 1

    # Check if the guessed letter is in the chosen word
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess

    # Show the current progress
    print(" ".join(display))

# Check if the player won or lost
if "_" not in display:
    print("Congratulations! You guessed the word.")
else:
    print("You've used all your attempts. Game over!")
    print(f"The word was: {chosen_word}")