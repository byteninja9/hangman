import random


word_list = ['camel', 'bird', 'yellow', 'green', 'car', 'cat', 'hello', 'word', 'world', 'football', 'computer', 'mango', 'banana', 'english', 'usa', 'weapon', 'monkey', 'key', 'random', 'python', 'javascript', 'earth', 'palnet', 'cow']

chosen_word = random.choice(word_list)


guess = input("Guess a letter: ").lower()



# Create Empty List called display

display = []

for _ in range(len(chosen_word)):
    display += "_"

#print(display)


for position in range(len(chosen_word)):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter

print(display)
