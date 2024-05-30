"""
Tic Tac Toe Player
"""
import copy
import math

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

    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    # if board is EMPTY, X has the first turn (start game)
    if x_count == 0 and o_count == 0:
        return 'X'

    # if the number of X's is greater than the number of O's, it is O's turn
    if x_count > o_count:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # set  empty board cells like possible action
    possible_action = set()

    # for i  (in with) <= 3  and if it  EMPTIES  this is possible to put X or O
    for i in range(len(board)):
        # for j (in height) <=3  and if it EMPTIES this is possible to put X or O
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_action.add((i, j))
    return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # if action is a not valid  raise an exception
    if action not in actions(board):
        raise ValueError("Invalid action")
    # make a copy board
    new_board = copy.deepcopy(board)
    # choose player
    current_player = player(board)
    # upgrade copy board and put player in cells action
    i, j = action
    new_board[i][j] = current_player
    # return updated copy board
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check Horizontally vertically and diagonally
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    # vertically
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    # diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    # if won X return X if O return O
    # if none won return none
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        if terminal(board):
            return utility(board)

        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))

        return v

    def min_value(board):
        if terminal(board):
            return utility(board)

        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))

        return v

    if terminal(board):
        return None

    current_player = player(board)
    best_action = None

    if current_player == 'X':
        best_value = float('-inf')
        for action in actions(board):
            action_value = min_value(result(board, action))
            if action_value > best_value:
                best_value = action_value
                best_action = action
    else:
        best_value = float('inf')
        for action in actions(board):
            action_value = max_value(result(board, action))
            if action_value < best_value:
                best_value = action_value
                best_action = action

    return best_action