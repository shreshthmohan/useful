#!/usr/bin/env python

from random import randint

board = []
board_rows = 6 # TODO: raw_input?
board_cols = 6 # TODO: raw_input?
for i in range(0, board_rows):
    board.append(["O"] * board_cols)

#print board

def print_board(brd):
    for row in brd:
        row = " ".join(row)
        print row
        
print_board(board)

print " "

board[3][2] = "X"
print_board(board)

def random_row(board):
    row_cnt = 0
    for row in board:
        row_cnt = row_cnt + 1
    return randint(0, row_cnt - 1)

def random_col(board):
    col_cnt = 0
    for col in board[1]:
        col_cnt = col_cnt + 1
    return randint(0, col_cnt - 1)

print random_row(board)
print random_col(board)


ship_row = random_row(board)
ship_col = random_col(board)


board[ship_row][ship_col] = "X"
print_board(board)


