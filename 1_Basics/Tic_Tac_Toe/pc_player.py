#!/usr/bin/env python3
"""
Module where a pc play the tic-tac-toe game.
For that we use the best strategy based on the wikipedia page.
Here is the link: https://en.wikipedia.org/wiki/Tic-tac-toe
"""

def is_winner(board, symbol):
    """
    Function to check if the current player won the game
    """

    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == symbol:
            return True

    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] == symbol:
            return True

    if board[0] == board[4] == board[8] == symbol:
        return True
    elif board[2] == board[4] == board[6] == symbol:
        return True

    return False

def available_move(board):
    """Return all the empty squares"""
    return [i for i in range(9) if board[i] not in ['x', 'o']]

def can_win(board, symbol):
    """Check if we can win in one move"""
    available = available_move(board)

    for pos in available:
        board_copy = board.copy()
        board_copy[pos] = symbol

        if is_winner(board_copy, symbol):
            return pos
        
    return None


def play_a_move(board, symbol):
    """
    Do a move based on the best possible strategy.
    
    Strategy priority (from Wikipedia):
    1. Win: If you can win, play to win
    2. Block: If opponent can win next turn, block them
    3. Fork: Create a fork (two ways to win)
    4. Block Fork: Block opponent's fork
    5. Center: Play center if available
    6. Opposite Corner: If opponent is in corner, play opposite corner
    7. Empty Corner: Play any empty corner
    8. Empty Side: Play any empty side
    """

    # 1. Win if we can do it in one move
    win_move = can_win(board, symbol)
    if win_move is not None:
        return win_move
  
    # 2. block the opponent if he can win next move











if __name__ == "__main__":
    play_a_move(board=["0", "1", "2", "x", "4", "5", "o", "7", "8"], symbol='x')

