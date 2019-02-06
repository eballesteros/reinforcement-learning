

def add_multiple_points(env, points,values):
    for point,value in zip(points,values):
        env.update_board(point,value)