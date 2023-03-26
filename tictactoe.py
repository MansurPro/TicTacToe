"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                count += 1
    if count % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                all_actions.add((i, j))
    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    possibleActions = actions(board)
    if action in possibleActions:
        boardCopy[action[0]][action[1]] = player(board)
        return boardCopy
    else:
        raise Exception("Sorry, board doesn't have this action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if len(set(i)) == 1 and list(set(i))[0] != EMPTY:
            return i[0]

    l = len(board[0])
    for i in range(l):
        col = [val[i] for val in board]
        if len(set(col)) == 1 and list(set(col))[0] != EMPTY:
            return col[0]

    diagonal = [board[i][i] for i in range(l)]
    mirrordiagonal = [board[l-1-i][i] for i in range(l-1,-1,-1)]
    if len(set(diagonal)) == 1 and list(set(col))[0] != EMPTY:
        return diagonal[0]
    if len(set(mirrordiagonal)) == 1 and list(set(col))[0] != EMPTY:
        return mirrordiagonal[0]

    #If there is no winner of the game
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = maxValue(board)
            return move
        else:
            value, move = minValue(board)
            return move

def maxValue(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    move = None
    for action in actions(board):
        val, atc = minValue(result(board, action))
        if val > v:
            v = val
            move = action
            if v == 1:
                return v, move
    return v, move

def minValue(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    move = None
    for action in actions(board):
        val, atc = maxValue(result(board, action))
        if val < v:
            v = val
            move = action
            if v == -1:
                return v, move
    return v, move
