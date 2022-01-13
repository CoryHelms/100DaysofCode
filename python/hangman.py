import random

words = ['football', 'baseball', 'bottle', 'glasses', 'wheels', 'blanket', 'library', 'picture', 'pumpkins', 'championship', 'leash', 'movies', 'guitars']

def game():
    #asking for player's name
    playerName = input("So you want to play hangman? What is your name? ")
    print("Hello,", playerName, "Welcome to the game!")

    #choosing a random word from the words list
    word = random.choice(words)
    wordLen = int(len(word))
    print("The word you are trying to guess has", wordLen, "letters.")

    #setting wrong guess counter
    wrongGuesses = 0
    #starting while loop for guessing:
    while wrongGuesses < 5:
        guess = input("Please guess a letter: ")
        if guess.lower() in word:
            print("Correct Guess")
            for letter in word:
                if guess.lower() == letter:
                    print(guess.lower())
                else:
                    print("_")
        else:
            print("Incorrect Guess")
            wrongGuesses += 1
            print("You have", 5 - wrongGuesses, "remaining.")

#main
game()