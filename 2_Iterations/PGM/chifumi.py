#!/usr/bin/env python3
"""Program to play at the game Chifumi with the machine"""

from random import randint, seed

def play_chifumi():
    """This is the function that is playing chifumi with the human user"""

    seed(24)

    print("" \
    "Welcome to the Chifumi game! \n" \
    "You can only play 3 different things:\n" \
    "1 = Rock\n" \
    "2 = Scissors\n" \
    "3 = Paper")

    while True:
        my_strategy = randint(1, 3)
        other_player = int(input("Enter a move!"))

        if my_strategy == 1:
            print("I play Rock!")
            if other_player == 3:
                print("You won the game!")
                break
            elif other_player == 2:
                print("I won the game!")
                break
            else:
                print("There is no winner, let's play again!")
                continue

        elif my_strategy == 2:
            print("I play Scissors!")
            if other_player == 1:
                print("You won the game!")
                break
            elif other_player == 3:
                print("I won the game!")
                break
            else:
                print("There is no winner, let's play again!")
                continue

        elif my_strategy == 3:
            print("I play Paper!")
            if other_player == 2:
                print("You won the game!")
                break
            elif other_player == 1:
                print("I won the game!")
                break
            else:
                print("There is no winner, let's play again!")
                continue

        else:
            print("Enter a valid input based on the rules please!")


if __name__ == "__main__":
    play_chifumi()
