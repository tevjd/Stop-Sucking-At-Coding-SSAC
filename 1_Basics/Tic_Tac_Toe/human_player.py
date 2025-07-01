#!/usr/bin/env python3
"""This is a module to let a human user play at tic-tac-toe"""


def play_a_move(board, symbol):
    """
    Function to play a move based on the board.
    A move is possible if a square doesn't have a symbol but an integer.
    """

    while True:
        move = int(input("Please give the move you want to do (number between 0 and 8): \n"))
        if board[move] not in ['x', 'o']:
            return move
        else:
            print("The move you gave isn't possible!")


if __name__ == "__main__":
    play_a_move(board=["0", "1", "2", "x", "4", "5", "o", "7", "8"], symbol='x')
