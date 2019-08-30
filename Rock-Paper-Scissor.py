def game(choice1, choice2):

    if choice1 == choice2:
        return ("null")

    elif choice1 == "rock":
        if choice2 == "paper":
            return ("The winner is player 2, Congratulation!")
        elif choice2 == "scissor":
            return ("The winner is player 1, Congratulation!")

    elif choice1 == "paper":
        if choice2 == "rock":
            return ("The winner is player 1, Congratulation!")
        elif choice2 == "scissor":
            return ("The winner is player 2, Congratulation!")

    elif choice1 == "scissor":
        if choice2 == "rock":
            return ("The winner is player 2, Congratulation!")
        elif choice2 == "paper":
            return ("The winner is player 1, Congratulation!")



Restart = "yes"
while Restart != "no" or winner == "null":
    player1 = input("First player(Rock, Paper or scissor?): ")
    player2 = input("Second player(Rock, Paper or Scissor?): ")

    winner = game(player1, player2)
    print(winner)

    if winner == "null":
        Restart = "yes"
        print("Retry!")

    else:
        print("")
        Restart = input("Restart game(yes/no): ")

    print("")