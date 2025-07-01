#!/usr/bin/env python3

"""A Tic-Tac-Toe game"""

# The different players are coded in python modules.
# The human player only ask the stdint to play.
# The pc_player play automatically and there is no special strategy.
import sys
import human_player
import pc_player
#import smart_pc_player


def get_the_char_to_display(symbol):
    """
    Return the chain of char based on the symbol.
    - 'x' = Unicode symbol for multiplication x in red.
    - 'o' = Unicode symbol for white circle o in white.
    - integer = return the integer.
    """
    red = '\033[31m'
    reset = '\033[0m'
    white = '\033[34m'

    if symbol == 'x':
        return f"{red}\u00D7{reset}"
    elif symbol == 'o':
        return f"{white}\u25CB{reset}"
    else:
        return symbol

def display_board(board):
    """
    Display the game board based on the list of 9 elements.
    This function display the board on the stdout with prints. 

    A valid symbol is an integer if the case is free. Or 'x' if the case
    is occupied by the player 1. Or 'o' if this is occupied by the palyer 
    2.
    """
    if len(board) != 9:
        raise ValueError(f"The length of the board is not correct: {len(board)}.")

    for i, item in enumerate(board):
        if isinstance(item, str):
            if item.lower() not in ['x', 'o', '0', '1', '2', '3', '4', '5', '6', '7', '8']:
                raise ValueError(f"The symbol is not x or o: {item}.")

    delimitation = '|-----|'

    # Print the upper-line of the board
    print(delimitation)

    # Print the core of the board
    for i, _ in enumerate(board):
        current_elem = get_the_char_to_display(board[i])

        if i in [0, 3, 6]:
            print('|', current_elem, sep='', end='')
        elif i in [1, 4, 7]:
            print('|', current_elem, '|', sep='', end='')
        elif i in [2, 5, 8]:
            print(current_elem, '|', sep='')

    # Print the below line
    print(delimitation)

def winning_chek(board, symbol):
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


def play_a_move(player, player_num, board, symbol):
    """Joue un coup.

    Cette fonction effectue les opérations suivantes tout en affichant
    ce qu'il se passe sur la sortie standard :
      - affiche le plateau représenté par board
      - utilise le module player pour savoir quel coup doit être joué
      - met à jour le plateau de jeu avec ce coup
      - affiche le plateau et le numéro du player gagnant si c'est gagné
        puis quitte le programme
      - renvoie le nouveau plateau

    précondition : player est un module avec une fonction
                   play_a_move(board, symbol) qui renvoie le
                   numéro d'une case précédemment inoccupée.
    précondition : player_num est soit l'entier 1 soit l'entier 2
    précondition : board est une list de 9 éléments
    précondition : symbol est soit "x" soit "o"

    """

    # First we display the board
    display_board(board)

    # We play a move according to the player and the symbol
    current_move = player.play_a_move(board, symbol)

    # Update the board
    board[current_move] = symbol

    # Check if there is a win
    is_winning = winning_chek(board, symbol)

    if is_winning:
        display_board(board)
        print(f"The player number {player_num} won the game!")
        sys.exit(0)
    else:
        return board


def play_game():
    """Play tic-tac-toe game"""

    # Init the game by asking the user to chose the player
    # We need the '{}' because of the splinting
    message_chose_player = (
        "Please give the type of player {} you want\n"
        "   0 for human\n"
        "   1 for simple pc\n"
        "   precise the number :"
    )

    print(message_chose_player.format(1), end="")
    type1 = int(input())
    print(message_chose_player.format(2), end="")
    type2 = int(input())
    player1 = (
        human_player
        if type1 == 0
        else (pc_player)
    )
    player2 = (
        human_player
        if type2 == 0
        else (pc_player)
    )
    print()

    # Init and display the board.
    # An empty place is giving by its number.
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # Play 9 times at max
    play_a_move(player1, 1, board, "x")
    play_a_move(player2, 2, board, "o")
    play_a_move(player1, 1, board, "x")
    play_a_move(player2, 2, board, "o")
    play_a_move(player1, 1, board, "x")
    play_a_move(player2, 2, board, "o")
    play_a_move(player1, 1, board, "x")
    play_a_move(player2, 2, board, "o")
    play_a_move(player1, 1, board, "x")

    # If we are here it's a draw
    print("Draw !")


if __name__ == "__main__":
    play_game()
    #display_board(["0", "1", "2", "x", "4", "5", "o", "7", "8"])
