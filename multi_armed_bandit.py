import numpy as np
import matplotlib.pyplot as plt

def incremental_average(old_average, new_value, n):
        return (1/n) * (((n - 1) * old_average) + new_value)

class Bandit():
    def __init__(self,real_mean):
        self.real_mean = real_mean
        self.estimated_mean = 0
        self.n_pulls = 0
        
    def pull(self):
        reward = np.random.normal(self.real_mean,1)
        self.update(reward)
        return reward
    
    def update(self, reward):
        self.n_pulls += 1
        self.estimated_mean = incremental_average(old_average = self.estimated_mean , new_value = reward, n = self.n_pulls)
        
    def __repr__(self):
        return 'Bandit with true mean {}. Estimated mean {} after {} pulls'.format(self.real_mean, self.estimated_mean, self.n_pulls)
    
def run_experiment(m1, m2, m3, epsilon, N):
    bandits = [Bandit(m) for m in [m1,m2,m3]]
    cumulative = np.empty(N)
    for i in range(N):
        if np.random.uniform() < epsilon: #explore
            bandit = np.random.choice(bandits)
        else:
            bandit = bandits[np.argmax([b.estimated_mean for b in bandits])]
        new_reward = bandit.pull()
        if i == 0:
            cumulative[i] = new_reward
        else:
            cumulative[i] = incremental_average(old_average = cumulative[i-1] , new_value = new_reward, n = i)
            
    plt.plot(cumulative)
    