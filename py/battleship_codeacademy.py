#Small Python project from codeacademy.com

from random import randint
import os

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    # Line below prints the random ship position
    # print(ship_row, ship_col)
    print_board(board)
    print ("Turn ", turn+1)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        os.system('clear')
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            os.system('clear')
            print ("You guessed that one already.")
            turn -= 1
        else:
            os.system('clear')
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print ("Game Over")
                break
        # Print (turn + 1) here!


board[ship_row][ship_col] = "B"
print_board(board)
