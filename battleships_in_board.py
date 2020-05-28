# Given an 2D board, count how many battleships are in it. The battleships are represented with 
# 'X's, empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, 
# they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

# Example:

# X..X
# ...X
# ...X
# In the above board there are 2 battleships.

# Invalid Example:

# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.


def vertical_cleanup(board, row, col):
   
    while row < len(board):
        if board[row][col] == 'X':
            board[row][col] = '.'
            row +=1
        else:
            return 
def horizantal_cleanup(board, row, col):
    
    while col < len(board[0]):
        if board[row][col] == 'X':
            board[row][col] = '.'
            col +=1
        else:
            return 


def find_battleships(board):
    print('board', board)
    ship_count = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            # print('[row][col]:', board[row][col])
            if board[row][col] == 'X':
                    ship_count+=1
                    if row+1 < len(board) and board[row+1][col] == 'X':
                        vertical_cleanup(board, row, col) #checks if ship is vertically long
                        # print('post VERTICAL cleanup:::::', board)
                        horizantal_cleanup(board, row, col)
                        # print('post HORIZANTAL cleanup:::::',board)
                    elif col+1 < len(board[0]) and board[row][col+1] == 'X':
                        horizantal_cleanup(board, row, col)
                        # print('post HORIZANTAL cleanup:::::',board)
                        vertical_cleanup(board, row, col) #checks if ship is vertically long
                        # print('post VERTICAL cleanup:::::', board)
                    
                
    print(board)
    return ship_count

# print(find_battleships([['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']]))
# print(find_battleships([["X","X","X"]]))

# : 72 ms, faster than 78.90% of Python3 online submissions for Battleships in a Board.

