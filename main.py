import random

import hangman_words
import hangman_art
from hangman_art import logo

end_of_game = False


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left. 
print(logo)
lives = 6


# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess in display:
        print(f"You've already guessed {guess}. Try again.")
        continue
    
    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        # If guess is not a letter in the chosen_word, reduce 'lives' by 1.
        # If lives go down to 0, the game should stop and it should print "You lose."
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if the user has got all the letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
