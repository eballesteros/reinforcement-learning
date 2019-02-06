import numpy as np

LENGTH = 3

class Agent():
    def __init__(self,value, strategy):
        self.value = value
        self.strategy = strategy
    
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
        self.o = -1
        
    def update_board(self,coordinates, value):
        x, y = coordinates
        self.board[y,x] = value
        
    def player_won(self, player_value):
        player_marks = self.board == player_value
        
        #check horzontal and vertical
        for ax in [0,1]:
            if (player_marks.sum(axis = ax) == 3).any():
                    return True
                
        #check diagonals
        if player_marks.diagonal().sum() == 3 or np.fliplr(player_marks).diagonal().sum() == 3:
            return True
        
        return False
    
    def get_empty_spots(self):
        return set(zip(np.where(self.board == 0)[1],np.where(self.board == 0)[0]))
        
    
    def draw_board(self):
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
        
        