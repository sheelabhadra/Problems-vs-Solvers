from typing import Dict, List
import numpy as np
from solvers.solver import Solver, Node, Graph
from collections import deque
import random
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Deep Q-learning Agent
class DQNAgent:
    def __init__(self, state_size, batch_size):
        self.state_size = state_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.01
        self.batch_size = 32
        self.model = self.build_model()

    def build_model(self, *args):
        pass

    def remember(self, state, reward, next_state, done):
        self.memory.append((state, reward, next_state, done))

    def act(self, h_values, states):
        """Returns the next state
            
        """
        if np.random.rand() <= self.epsilon:
            idx = random.randrange(len(states))
            return states[idx], h_values[idx]
        else:
            idx = np.argmin(h_values)
            return states[idx], h_values[idx]

    def replay(self):
        minibatch = random.sample(self.memory, self.batch_size)
        states, targets = [], []
        for state, reward, next_state, done in minibatch:
            if not done:
                next_state = np.reshape(next_state, [1, self.state_size])
                # target = reward + self.gamma*self.model.predict(next_state)
                target = self.model.predict(next_state, batch_size=1)
            else:
                target = reward
            states.append(state)
            targets.append(target[-1][-1])
        states, targets = np.array(states), np.array(targets)
        history = self.model.fit(states, targets, batch_size=self.batch_size, epochs=1, verbose=0)
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


class LRTAStar(Solver):
    def __init__(self):
        super().__init__()
        self.cost_table = {}

    """
    def solve(self, start_state, goal_state):
        # No lookahead version
        start_node = Node(start_state)
        goal_node = Node(goal_state)

        queue = []

        while True:
            self.nodes_expanded = 0
            self.cost = float('inf')
            current_node = start_node

            while not current_node.isGoal(goal_node):
                self.nodes_expanded += 1

                neighbors = current_node.getNeighbors(current_node.state, goal_node.state, self.use_heuristic_cost)
                current_node.h = float('inf')

                if neighbors:
                    for neighbor in neighbors:
                        if neighbor in self.cost_table:
                            neighbor_f = neighbor.g + self.cost_table[neighbor]
                        else:
                            neighbor_f = neighbor.g + neighbor.h

                        if neighbor_f < current_node.h:
                            current_node.h = neighbor_f
                            next_node = neighbor
                    
                    self.cost_table[current_node] = current_node.h
                    self.graph.setParent(current_node, next_node)

                    current_node = next_node

            self.optimal_path = self.get_optimal_path(current_node)
            self.cost = self.nodes_expanded
            queue.append(self.cost)

            if len(queue) >= 10:
                last = queue[-10:]
                if len(set(last)) == 1:
                    print(self.cost_table)
                    return
    """
    
    def solve(self, start_state, goal_state):
        start_node = Node(start_state)
        goal_node = Node(goal_state)

        episodes = 200
        batch_size = 32
        agent = DQNAgent(len(start_node.state), batch_size)

        H_history = []

        # Iterate the game
        for e in range(episodes):
            # reset state in the beginning of each game
            nodes_expanded = 0
            cost = float('inf')
            current_node = start_node

            done = 0
            time_t = 0
            while not current_node.isGoal(goal_node) and time_t < 1000:
                nodes_expanded += 1

                neighbors = current_node.getNeighbors(current_node.state, goal_node.state, self.use_heuristic_cost)

                if neighbors:
                    H_values = []
                    for neighbor in neighbors:
                        #choose an action epsilon greedy
                        state = np.reshape(neighbor.state, [1, agent.state_size])
                        h_pred = agent.model.predict(state)
                        H_values.append(h_pred)

                    next_node, h_value = agent.act(H_values, neighbors)
                    self.graph.setParent(current_node, next_node)
                    agent.remember(current_node.state, h_value, next_node.state, done)
                    
                    current_node = next_node
                    time_t += 1

            if current_node.isGoal(goal_node):
                done = 1
                # determine how to add the h value to the replay memory after you reach the goal
                agent.remember(current_node.state, [[0.0]], None, done)
            
            cost = nodes_expanded
            # print the score and break out of the loop
            if not e%10:
                print("episode: {}/{}, cost: {}".format(e, episodes, cost))

            if len(agent.memory) >= agent.batch_size:
                agent.replay()
                H_history.append(agent.model.predict(np.reshape(start_node.state, [1, agent.state_size]), batch_size=1)[-1])

        # Plot training loss values
        plt.plot(H_history)
        plt.title('Heuristic value')
        plt.ylabel('H')
        plt.xlabel('Episode')
        plt.show()