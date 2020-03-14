import itertools
from colorama import Fore, Back, Style


def win(current_game):


    def all_same(l, st):
        if l.count(l[0]) == len(l) and l[0] != 0:
            print(f"Player {l[0]} is the winner {st}!")
            return True


    # Horizontal:
    for row in game:
        if all_same(row, "horizontally"):
            return True

    # Vertical:
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check, "vertically"):
            return True

    # Diagonal:
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags, "diagonally(/)"):
        return True

    diags = []
    for idx in range(len(game)):
        diags.append(game[idx][idx])
    if all_same(diags, "diagonally(\\)"):
        return True

    return False


## GAME:
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("The position is occupado! Choose another!")
            return game_map, False 
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display: 
            game_map[row][column] = player
        for count, row in enumerate(game_map):
        	colored_row = ""
        	for item in row:
        		if item == 0:
        			colored_row += "   "
        		elif item == 1:
        			colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
        		elif item == 2:
        			colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
        	print(count,colored_row)
        return game_map, True 

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2.", e)       
        return game_map, False   
    
    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game_size = int(input("What size of game tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False 

        while not played:
            column_choice = int(input("what column do you wanna play? (0, 1, 2): "))
            row_choice = int(input("what row do you wanna play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            again = input("Game over. Do you wanna play again?(y/n): ")
            if again.lower() == "y":
                print("Restarting")
            else:
                print("Game shutting down")
                play = False