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


def can_block_opponent(board, symbol):
    """Function to check if we need to block the opponent for the next move"""
    opponent_symbol = 'x' if symbol == 'o' else 'o'
    return can_win(board, opponent_symbol)


def can_fork(board, symbol):
    """
    Function to check if we can create a fork.
    A fork is when we have two ways to win.
    """
    available = available_move(board)

    for pos in available:
        board_copy = board.copy()
        board_copy[pos] = symbol

        win_count = 0
        for check_pos in available_move(board_copy):
            test_board = board_copy.copy()
            test_board[check_pos] = symbol
            if is_winner(test_board, symbol):
                win_count += 1

        if win_count >= 2:
            return pos

    return None

def can_block_fork(board, symbol):
    """Function to check if we can block an opponent's fork"""
    opponent_symbol = 'x' if symbol == 'o' else 'o'

    fork_pos = can_fork(board, opponent_symbol)
    if fork_pos is not None:
        return fork_pos

    available = available_move(board)

    for pos in available:
        board_copy = board.copy()
        board_copy[pos] = symbol

        # check if this create a threat for the opponent
        if interesting_move := can_win(board_copy, symbol):
            #simulate opponent's response
            opponent_response = interesting_move
            if opponent_response is not None:
                #after opponent's response, can they still fork?
                board_after_block = board_copy.copy()
                board_after_block[opponent_response] = opponent_symbol

                if can_fork(board_after_block, opponent_symbol) is None:
                    return pos

    return None

def play_center(board):
    """Function that check the center"""
    if board[4] not in ['x', 'o']:
        return 4
    return None

def is_in_corner(board, symbol):
    """Check if the opponent is in corner"""
    opponent_symbol = 'x' if symbol == 'o' else 'o'

    corners = [(0, 8), (2, 6), (6, 2), (8, 0)]

    for corner, opposite in corners:
        if (board[corner] == opponent_symbol and board[opposite] not in ['x', 'o']):
            return opposite

    return None

def check_corner(board):
    """Chekc if one corner is empty"""
    corners = [0, 2, 6, 8]

    for corner in corners:
        if board[corner] not in ['x', 'o']:
            return corner

    return None

def check_side(board):
    """Function to check if one side is empty"""

    sides = [1, 3, 5, 7]
    for side in sides:
        if board[side] not in ['x', 'o']:
            return side
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
    block_move = can_block_opponent(board, symbol)
    if block_move is not None:
        return block_move

    # 3. Create a fork = 2 ways to win
    fork_move = can_fork(board, symbol)
    if fork_move is not None:
        return fork_move

    # 4. Block opponent's fork
    block_fork_move = can_block_fork(board, symbol)
    if block_fork_move is not None:
        return block_fork_move

    # 5. Play center is available
    center_move = play_center(board)
    if center_move is not None:
        return center_move

    # 6. Play opposite corner
    opposite_corner_move = is_in_corner(board, symbol)
    if opposite_corner_move is not None:
        return opposite_corner_move

    # 7. Play corner
    corner_available = check_corner(board)
    if corner_available is not None:
        return corner_available

    # 8. Play side
    side_available = check_side(board)
    if side_available is not None:
        return side_available

    # In case of error we just play the first possible move
    # This should not happend here.
    print("Error: there is no strategy possible.")
    return available_move(board)[0]


if __name__ == "__main__":
    play_a_move(board=["0", "1", "2", "x", "4", "5", "o", "7", "8"], symbol='x')
