#!/usr/bin/env python3

"""A Tic-Tac-Toe game"""

# The different players are coded in python modules.
# The human player only ask the stdint to play.
# The pc_player play automatically and there is no special strategy.
import human_player
import pc_player
import smart_pc_player


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


def joue_coup(joueur, joueur_num, cases, symbol):
    """Joue un coup.

    Cette fonction effectue les opérations suivantes tout en affichant
    ce qu'il se passe sur la sortie standard :
      - affiche le plateau représenté par cases
      - utilise le module joueur pour savoir quel coup doit être joué
      - met à jour le plateau de jeu avec ce coup
      - affiche le plateau et le numéro du joueur gagnant si c'est gagné
        puis quitte le programme
      - renvoie le nouveau plateau

    précondition : joueur est un module avec une fonction
                   joue_coup(cases, symbol) qui renvoie le
                   numéro d'une case précédemment inoccupée.
    précondition : joueur_num est soit l'entier 1 soit l'entier 2
    précondition : cases est une list de 9 éléments
    précondition : symbol est soit "x" soit "o"

    """
    # TODO
    ...




def joue_partie():
    """Joue une partie complète de morpion"""

    # Initialisation des deux joueurs en demandant à l'utilisateur
    # Parenthèses nécessaires pour "spliter un string literal"
    message_choix_joueur = (
        "Veuillez choisir le type du joueur {} en tapant\n"
        "  0 pour humain\n"
        "  1 pour un ordinateur\n"
        "  2 pour un ordinateur très malin\n"
        "  entrez votre choix : "
    )

    print(message_choix_joueur.format(1), end="")
    type1 = int(input())
    print(message_choix_joueur.format(2), end="")
    type2 = int(input())
    joueur1 = (
        human_player
        if type1 == 0
        else (pc_player if type1 == 1 else smart_pc_player)
    )
    joueur2 = (
        human_player
        if type2 == 0
        else (pc_player if type2 == 1 else smart_pc_player)
    )
    print()

    # Initialisation et affichage du plateau vide
    # Une case vide est représentée par son numéro,
    # utilisé par le joueur humain pour indiquer
    # quelle case il joue.
    cases = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # Joue 9 coups au maximum
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    joue_coup(joueur1, 1, cases, "x")

    # Si on arrive là, il y a égalité
    print("Match nul !")


if __name__ == "__main__":
    #joue_partie()
    display_board(["0", "1", "2", "x", "4", "5", "o", "7", "8"])
