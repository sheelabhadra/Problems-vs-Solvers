from typing import Dict, List
from solvers.solver import Solver, Node, Graph
from solvers.ucs import *
from solvers.astar import *
from solvers.rtastar import *
from solvers.lrtastar import *
import timeit

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


def gap_heuristic(state, goal_state):
    state_cpy = state[:]
    state_cpy.append(len(state_cpy)+1)
    cost = 0
    for i in range(len(state_cpy)-1):
        if abs(state_cpy[i+1] - state_cpy[i]) > 1:
            cost += 1
    return cost


def _hash(self):
    return str(self.state)


def _getNeighbors(self, state, goal_state, use_heuristic_cost, state_cost=0):
    len_state, states = len(state), []

    for i in range(1, len_state):
        sub_list = state[0:i+1]

        tail_list = state[i+1:len_state]

        # flip the state
        sub_list = sub_list[::-1]

        # concatenate the two lists to obtain the new state
        list_state = sub_list + tail_list

        g_cost = state_cost + 1 # i+1
        
        if use_heuristic_cost == "gap":
            h_cost = gap_heuristic(list_state, goal_state)
        else:
            h_cost = 0

        list_state = Node(list_state)
        list_state.g, list_state.h = g_cost, h_cost

        states.append(list_state) # cost: number of flips

    # if len(states):
    #     states.pop(0) # removes the first state which is the same as the statezs

    return states


def _build_model(self):
    # Neural Net for Deep-Q learning Model
    model = Sequential()
    model.add(Dense(32, input_dim=self.state_size, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
    return model


def run_solver(start_state, goal_state, solver, heuristic):
    """
    Should only contain the start state, the goal state, and the solver as input
    
    """
    Node.getNeighbors = _getNeighbors
    Node.hash = _hash

    DQNAgent.build_model = _build_model
    
    pancake_solver = solver
    pancake_solver.use_heuristic_cost = heuristic
    pancake_solver.solve(start_state, goal_state)
    stats = pancake_solver.get_statistics()
    return stats
