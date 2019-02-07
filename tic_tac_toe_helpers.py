import numpy as np

def add_multiple_points(env, points,values):
    for point,value in zip(points,values):
        env.update_board(point,value)
        
def state_to_board(state):
    if state == 0:
        return np.repeat(0,9).reshape((3,3))
    digits = []
    while state:
        digits.append(int(state % 3))
        state //= 3
    return np.concatenate((np.array(digits), np.repeat(0,9-len(digits)))).reshape((3,3))

def board_to_state(board):
    flat_board = board.flatten()
    return (flat_board * np.power(3,np.linspace(0,flat_board.size-1,flat_board.size))).astype(np.int32).sum()

def _player_won(player_value,board):
    player_marks = board == player_value
        
    #check horzontal and vertical
    for ax in [0,1]:
        if (player_marks.sum(axis = ax) == 3).any():
                return True

    #check diagonals
    if player_marks.diagonal().sum() == 3 or np.fliplr(player_marks).diagonal().sum() == 3:
        return True

    return False

def switch_value(value):
    if value == 1:
        return 2
    return 1