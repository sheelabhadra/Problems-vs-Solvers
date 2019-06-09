from typing import Dict, List
from solvers.solver import Solver, Node, Graph
from solvers.ucs import *
from solvers.astar import *
import timeit

def _getNeighbors(self, state: List[int], dict_predecessors: Dict[str, List], use_heuristic_cost, goal_state: List[int]) -> List[List[int]]:
    len_state, states = len(state), []

    for i in range(1, len_state):
        sub_list = state[0:i+1]
        len_sub_list = len(sub_list)

        tail_list = state[i+1:len_state]

        # flip the state
        sub_list = sub_list[::-1]

        # concatenate the two lists to obtain the new state
        list_state = sub_list + tail_list

        # insert the states and the edge cost if the state does not exist in dict_predecessors
        # if str(list_state) not in dict_predecessors:
        g_cost = 1 # i+1
        h_cost = 0
        if use_heuristic_cost:
            for i in range(len(list_state)):
                if list_state[i] != goal_state[i]:
                    h_cost += 1

        f_cost = g_cost + h_cost
        list_state = Node(list_state)
        list_state.g, list_state.h = g_cost, h_cost

        states.append((list_state)) # cost: number of flips

    # if len(states):
    #     states.pop(0) # removes the first state which is the same as the state

    return states

def run_solver(start_state, goal_state, solver):
    """
    Should only contain the start state, the goal state, and the solver as input
    
    """
    Node.getNeighbors = _getNeighbors
    
    pancake_solver = solver
    pancake_solver.solve(start_state, goal_state)
    stats = pancake_solver.get_statistics()
    print('PANCAKE')
    print(stats)
