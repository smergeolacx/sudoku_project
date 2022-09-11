from settings import *

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    xth_sq = pos[1] // 3
    yth_sq = pos[0] // 3

    for i in range(yth_sq*3, yth_sq*3 + 3):
        for j in range(xth_sq * 3, xth_sq*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True



def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

solution = solve(prob_2)