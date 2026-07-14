import random

word_list = ["python", "college", "laptop", "coding", "student"]

secret_word = random.choice(word_list)

guessed_letters = ""
chances = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time")

while chances > 0:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nYou Won!")
        print("The word was:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters += guess

    if guess not in secret_word:
        chances -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", chances)

if chances == 0:
    print("\nGame Over!")
    print("The correct word was:", secret_word)