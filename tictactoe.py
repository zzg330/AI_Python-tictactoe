"""
Tic Tac Toe Player
"""

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
    count_x = 0
    count_o = 0
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)
    if count_x == count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                act = (i, j)
                actions.add(act)
    # sorted(actions) can put (0,0) as the first element in the returned set.
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = []

    for row in board:
        new_board.append(row[:])
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == len(row):
            return X
        if row.count(O) == len(row):
            return O
    for j in range(len(board[0])):
        col_win_x = 0
        col_win_o = 0
        for i in range(len(board)):
            if board[i][j] == X:
                col_win_x += 1
            if board[i][j] == O:
                col_win_o += 1
        if col_win_x == len(board):
            return X
        if col_win_o == len(board):
            return O

    col_win_x = 0
    col_win_o = 0
    for i in range(len(board)):
        if board[i][i] == X:
            col_win_x += 1
        if board[i][i] == O:
            col_win_o += 1

    if col_win_x == len(board):
        return X
    if col_win_o == len(board):
        return O

    col_win_x = 0
    col_win_o = 0
    num = len(board)
    for i in range(num):
        if board[i][num - 1 - i] == X:
            col_win_x += 1
        if board[i][num - 1 - i] == O:
            col_win_o += 1
    if col_win_x == len(board):
        return X
    if col_win_o == len(board):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)
    if winner(board) == None and empty_count > 0:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == None:
        return 0
    elif winner(board) == X:
        return 1
    else:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    state_value = []
    state_location = []
    for action in actions(board):
        if player(board) == X:
            min_value_state = min_value(result(board, action))
            state_value.append(min_value_state)
            state_location.append(action)
        if player(board) == O:
            max_value_state = max_value(result(board, action))
            state_value.append(max_value_state)
            state_location.append(action)

    if player(board) == X:
        index = state_value.index(max(state_value))
        # print("X States and its corresponding values are:")
        # print(state_value)
        # print(state_location)
        return (state_location[index])

    if player(board) == O:
        index = state_value.index(min(state_value))
        # print("O Sates and its corresponding values are:")
        # print(state_value)
        # print(state_location)

        return (state_location[index])


def max_value(board):
    v = -math.inf
    if terminal(board):
        v = utility(board)
    else:
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
            # Interrupt the loop when finding the maximum one, which can improve the performance (8736/56730)
            if v == 1:
                break
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        v = utility(board)
    else:
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
            # Interrupt the loop when finding the minimum one, which can improve the performance (8736/56730)
            if v == -1:
                break
    return v
