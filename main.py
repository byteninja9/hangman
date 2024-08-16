import random

from hangman_word import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)


print(logo)
lives = 6


display = []
for _ in range(len(chosen_word)):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ")

    if guess in display:
        print(f"You've already guessed {guess}. Try again.")
        continue

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")
    
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")


