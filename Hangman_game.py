import random

# List of predefined words
words = ["python", "django", "computer", "program", "developer"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("Welcome to Hangman!")
print("You have 6 incorrect guesses.")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter exists in word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)