import random

#Rock Paper Scissors
def game():
    choices = ["Rock", "Paper", "Scissors"]

    compChoice = random.choice(choices)

    userChoice = input("Do you choose Rock, Paper, or Scissors? (Type Answer): ")

    if userChoice == "Rock" and compChoice == "Scissors" or \
       userChoice == "Paper" and compChoice == "Rock" or \
       userChoice == "Scissors" and compChoice == "Paper":
        print("You chose:", userChoice)
        print("They chose:", compChoice)
        print("You win!\n")
        
        playAgain = input("Do you want to play again? (y/n): ")
        if playAgain == "y":
            game()
        else:
            print("Thanks for playing!")
    elif compChoice == "Rock" and userChoice == "Scissors" or \
         compChoice == "Paper" and userChoice == "Rock" or \
         compChoice == "Scissors" and userChoice == "Paper":
        print("You chose:", userChoice)
        print("They chose:", compChoice)
        print("You Lose!\n")

        playAgain = input("Do you want to play again? (y/n): ")
        if playAgain == "y":
            game()
        else:
            print("Thanks for playing!")
    elif userChoice == compChoice:
        print("You chose:", userChoice)
        print("They chose:", compChoice)
        print("It's a tie!\n")

        playAgain = input("Do you want to play again? (y/n): ")
        if playAgain == "y":
            game()
        else:
            print("Thanks for playing!")

#main
game()
