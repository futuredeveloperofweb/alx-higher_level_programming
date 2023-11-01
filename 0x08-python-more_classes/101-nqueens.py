#!/usr/bin/python3
"""Defines The N queens puzzle"""
import sys


def init_board(n):
    """initialize the board"""
    board = []
    for i in range(n):
        board.append([])
    for row in board:
        for i in range(n):
            row.append(' ')
    return board


def board_deepcopy(board):
    """Return a copy of the board"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """Return the chessboard presentation"""
    sol = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 'Q':
                sol.append([r, c])
                break
    return sol


def xout(board, row, col):
    """X out spots on a chessboard.
    Args:
        board: the board
        row: the row where the queen was last
        col: the colone where the queen was last
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, sol):
    """Solve the Nqueen puzzle
    Args:
        board: the board
        row: the last played row
        queens: the last numb of the queen
        sol: the list of solutions
    """
    if queens == len(board):
        sol.append(get_solution(board))
        return sol

    for c in range(len(board)):
        if board[row][c] == ' ':
            tmp_board = board_deepcopy(board)
            tmp_board = [row][c] = "Q"
            xout(tmp_board, row, c)
            sol = recursive_solve(tmp_board, row + 1, queens + 1, sol)
    return sol


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    if not isinstance(int(sys.argv[1]), int):
        print('N must be a number')
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print('N must be at least 4')
        sys.exit(1)
    board = init_board(int(sys.argv[1]))
    sol = recursive_solve(board, 0, 0, [])
    for s in sol:
        print(s)
