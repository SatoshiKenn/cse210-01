"""
Kennette Guevara - W02 Prove: Developer - Solo Code Submission
"""

#Module to print with colors
import colorama
from colorama import Fore

def displayBoard(grid):
    print(Fore.BLACK + f"{grid[0]}|{grid[1]}|{grid[2]}\n-+-+-\n{grid[3]}|{grid[4]}|{grid[5]}\n-+-+-\n{grid[6]}|{grid[7]}|{grid[8]}")


def xTurn(grid, space):
    spaceIndex = int(space) - 1
    grid[spaceIndex] = "X"

    displayBoard(grid)


def oTurn(grid, space):
    spaceIndex = int(space) - 1
    grid[spaceIndex] = "O"

    displayBoard(grid)


def main():
    """
    While loop to make the game,
    if it's an odd number will be x's turn
    if it's and even number will be o's turn
    """
    tictactoe = ["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]

    displayBoard(tictactoe)

    game = True
    turn = 0
    while game == True:
        if turn <= 8:
            if (turn % 2) == 0:
                space = input(Fore.BLUE + "x's turn to choose a square (1-9):")
                spaceIndex = int(space) - 1
                if tictactoe[spaceIndex] == "X" or tictactoe[spaceIndex] == "O":
                    print("Square already in use, please select again.")
                else:
                    xTurn(tictactoe, space)
                    if (tictactoe[0] == "X" and tictactoe[1] == "X" and tictactoe[2] == "X") or (tictactoe[3] == "X" and tictactoe[4] == "X" and tictactoe[5] == "X") or (tictactoe[6] == "X" and tictactoe[7] == "X" and tictactoe[8] == "X") or (tictactoe[0] == "X" and tictactoe[3] == "X" and tictactoe[6] == "X") or (tictactoe[0] == "X" and tictactoe[4] == "X" and tictactoe[8] == "X") or (tictactoe[2] == "X" and tictactoe[4] == "X" and tictactoe[6] == "X") or (tictactoe[2] == "X" and tictactoe[5] == "X" and tictactoe[8] == "X"):
                        print(Fore.BLUE + "Player one wins! Good game. Thanks for playing!")
                        game = False
                    else:
                        turn += 1
                        print(f"Turn: {turn}")
            elif (turn % 2) != 0:
                space = input(Fore.RED + "o's turn to choose a square (1-9):")
                spaceIndex = int(space) - 1
                if tictactoe[spaceIndex] == "X" or tictactoe[spaceIndex] == "O":
                    print("Square already in use, please select again.")
                else:
                    oTurn(tictactoe, space)
                    if (tictactoe[0] == "O" and tictactoe[1] == "O" and tictactoe[2] == "O") or (tictactoe[3] == "O" and tictactoe[4] == "O" and tictactoe[5] == "O") or (tictactoe[6] == "O" and tictactoe[7] == "O" and tictactoe[8] == "O") or (tictactoe[0] == "O" and tictactoe[3] == "O" and tictactoe[6] == "O") or (tictactoe[0] == "O" and tictactoe[4] == "O" and tictactoe[8] == "O") or (tictactoe[2] == "O" and tictactoe[4] == "O" and tictactoe[6] == "O") or (tictactoe[2] == "O" and tictactoe[5] == "O" and tictactoe[8] == "O"):
                        print(Fore.RED + "Player two wins! Good game. Thanks for playing!")
                        game = False
                    else:
                        turn += 1
                        print(f"Turn: {turn}")
        else:
            print("DRAW!")
            game = False


if __name__ == "__main__":
    main()
