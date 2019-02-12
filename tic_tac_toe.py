from tqdm import tqdm
from random import shuffle
import numpy as np
from tic_tac_toe_helpers import state_to_board, board_to_state, _player_won, switch_value

LENGTH = 3

_valid_strategies = ['random','epsilon-greedy']

class Agent():
    def __init__(self,value, strategy, verbose = True, epsilon = None, alpha = None):
        self.value = value
        self.verbose = verbose
        
        self.strategy = strategy
        if self.strategy not in _valid_strategies:
            raise ValueError('{} not a valid strategy. Valid strategies: {}'.format(self.strategy, str(_valid_strategies)))
        if self.strategy == 'epsilon-greedy':
            if epsilon is None or alpha is None:
                raise ValueError('For epsilon-greedy you need to pass espilon and alpha')
            self.epsilon = epsilon
            self.alpha = alpha
            self.value_function = self.initialize_value_function()
    
    def get_state_initial_value(self,state):
        board = state_to_board(state)
        if _player_won(self.value, board):
            return 1
        if _player_won(switch_value(self.value), board):
            return 0
        if (board != 0).all():
            return 0
        return 0.5
    
    def initialize_value_function(self):
        return {state:self.get_state_initial_value(state) for state in tqdm(range(3**9))}
    
    def make_decision(self, env):
        if self.strategy == 'random':
            return self.make_random_decision(env)
        
        else: #epsilon-greedy strat
            p = np.random.random()
            if p < self.epsilon:
                if self.verbose:
                    print('Random decision')
                return self.make_random_decision(env)
            else:
                if self.verbose:
                    env.board.draw(transition_values = self.get_transition_values(env))
                empty_spots = list(env.get_empty_spots())
                shuffle(empty_spots)
                possible_states = [env.board.get_updated(spot,self.value).to_state() for spot in empty_spots]
                return empty_spots[np.argmax(np.array([self.value_function[state] for state in possible_states]))]
                
    
    def make_random_decision(self,env):
        empty_spots = env.get_empty_spots()
        random_index = np.random.randint(len(empty_spots))
        return list(empty_spots)[random_index]
    
    
    def get_transition_values(self,env):
        transition_values = np.ones((3,3))*-1
        empty_spots = env.get_empty_spots()
        for spot in empty_spots:
            transition_values[spot] = self.value_function[env.board.get_updated(spot,self.value).to_state()]
        return transition_values.T
        
    def play(self,env):
        point = self.make_decision(env)
        env.update_board(point, self.value)
    
    def __repr__(self):
        return 'Agent {}'.format(self.value)
    
class Board():
    def __init__(self, values = None):
        self.x = 1
        self.o = 2
        if values is None:
            self.values = np.zeros((3,3))
        else:
            self.values = values
        
    def __call__(self):
        return self.values
    
    def update(self,coordinates,value):
        x, y = coordinates
        self.values[y,x] = value
        
    def get_updated(self, coordinates,value):
        updated = self.copy()
        updated.update(coordinates,value)
        return updated
        
        
    def to_state(self):
        return board_to_state(self.values)
    
    def copy(self):
        return Board(values = self.values.copy())
    
    def draw(self, transition_values = None):
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print("| ", end="")
                if self.values[i,j] == self.x:
                    print("x ", end="")
                elif self.values[i,j] == self.o:
                    print("o ", end="")
                else:
                    if transition_values is None:
                        print("  ", end="")
                    else:
                        print("{:.2f}".format(transition_values[i,j]), end = "")
            print("|")
        print("-------------")
    

class Enviroment():
    def __init__(self):
        self.board = Board()
        self.x = 1
        self.o = 2
        
    def update_board(self,coordinates, value):
        self.board.update(coordinates,value)
        
    def player_won(self, player_value):
        return _player_won(player_value, self.board())
    
    def get_empty_spots(self):
        return set(zip(np.where(self.board() == 0)[1],np.where(self.board() == 0)[0]))
    
    def get_state(self):
        return self.board.to_state()
    
    def draw_board(self):
        self.board.draw()
        
def play_game(agent1, agent2, enviroment, wait = False):
    
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
        if wait:
            input()
    
    print("THIS IS A TIE!")
    return
        
        