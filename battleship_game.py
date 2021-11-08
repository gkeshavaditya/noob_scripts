# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Keshavaditya Golla"
__email__ = "keshav.aditya19@gmail.com"

from random import randint


def create_board():
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    return board


def print_board(board):
    for row in board:
        print("  ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def add_battleship_to_board(board):
    return random_row(board), random_col(board)


if __name__ == "__main__":

    board = create_board()
    print_board(board)

    ship_row, ship_col = add_battleship_to_board(board)

    for turn in range(5):
        print("Turn", turn + 1)
        print("Guess which row and column position in the 5x5 board is the battleship located")
        guess_row = int(input("Row: ")) - 1
        guess_col = int(input("Col: ")) - 1
        if (guess_row == ship_row) and (guess_col == ship_col):
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn + 1 == 3:
                print("Game Over")
                print("Here was the ship(#)")
                board[ship_row][ship_col] = "#"
                print_board(board)
                break

            print_board(board)
