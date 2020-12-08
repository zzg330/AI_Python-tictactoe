from tictactoe import *

board=[[None, X, O], [O, X, None],[X,None , O]]
print("Original Board is")
for b1 in board:
    print(b1)
# print(board)
print("Current Player is", player(board))

print("Possible Actions in this state of board are: ")
print(actions(board))
"""
print("Original Board is")
print(board)

new_board = result(board, action=(0, 0))
print("New Board is")
print(new_board)
"""
print(f'Winner is: player {winner(board)}')
print(f"Utility of Board is", utility(board))
print(f"Is it a terminal board", terminal(board))

print('\n')

print("Maximum Value of Board is")
print(max_value(board))
print("Minimum Value of Board is")
print(min_value(board))
print("**********************")
act = minimax(board)
print("Optimum Move is")
print(act)
for row in result(board, act):
    print(row)