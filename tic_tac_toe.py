from tqdm import tqdm
import numpy as np
from tic_tac_toe_helpers import state_to_board, board_to_state, _player_won, switch_value

LENGTH = 3

class Agent():
    def __init__(self,value, strategy):
        self.value = value
        self.strategy = strategy
        self.value_function = self.initialize_value_function()
    
    def get_state_value(self,state):
        board = state_to_board(state)
        if _player_won(self.value, board):
            return 1
        if _player_won(switch_value(self.value), board):
            return 0
        if (board != 0).all():
            return 0
        return 0.5
    
    def initialize_value_function(self):
        return {state:self.get_state_value(state) for state in tqdm(range(3**9))}
    
    def make_decision(self, env):
        if self.strategy == 'random':
            empty_spots = env.get_empty_spots()
            random_index = np.random.randint(len(empty_spots))
            return list(empty_spots)[random_index]
        
    def play(self,env):
        point = self.make_decision(env)
        env.update_board(point, self.value)
    
    def __repr__(self):
        return 'Agent {}'.format(self.value)

class Enviroment():
    def __init__(self):
        self.board = np.zeros((3,3))
        self.x = 1
        self.o = 2
        
    def update_board(self,coordinates, value):
        x, y = coordinates
        self.board[y,x] = value
        
    def player_won(self, player_value):
        return _player_won(player_value, self.board)
    
    def get_empty_spots(self):
        return set(zip(np.where(self.board == 0)[1],np.where(self.board == 0)[0]))
    
    def get_state(self):
        return board_to_state(self.board)
    
    def draw_board(self):
        print("State {}".format(self.get_state()))
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print("| ", end="")
                if self.board[i,j] == self.x:
                    print("x ", end="")
                elif self.board[i,j] == self.o:
                    print("o ", end="")
                else:
                    print("  ", end="")
            print("|")
        print("-------------")
        
def play_game(agent1, agent2, enviroment):
    
    print('Agent {}, strategy {}\tvs\tAgent {}, strategy {}'.format(agent1.value,agent1.strategy,agent2.value,agent2.strategy))
    print('{} -> x, {} -> o'.format(enviroment.x,enviroment.o))
    print()
    
    agents = [agent1,agent2]
    agent_index = np.random.randint(2)
    
    for turn in range(9):
        agent_index = (agent_index+1)%2 #swap index
        playing_agent = agents[agent_index]
        print("{}'s turn".format(playing_agent))
        
        playing_agent.play(enviroment)
        enviroment.draw_board()
        
        if enviroment.player_won(playing_agent.value):
            print("{} WON!".format(playing_agent))
            return
        print()
    
    print("THIS IS A TIE!")
    return
        
        