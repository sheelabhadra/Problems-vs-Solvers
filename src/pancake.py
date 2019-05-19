from typing import Dict, List
from ucs import *
from solver import *
import timeit

def _getNeighbors(self, state: List[int], dict_predecessors: Dict[str, List], use_heuristic_cost) -> List[List[int]]:
    len_state, states = len(state), []

    for i in range(len_state):
        sub_list = state[0:i+1]
        len_sub_list = len(sub_list)

        tail_list = state[i+1:len_state]

        # flip the state
        sub_list = sub_list[::-1]

        # concatenate the two lists to obtain the new state
        list_state = sub_list + tail_list

        # insert the states and the edge cost if the state does not exist in dict_predecessors
        if str(list_state) not in dict_predecessors:
            g_cost = 1 # i+1 
            if use_heuristic_cost:
                h_cost = 0                
            else:
                h_cost = 0
            f_cost = g_cost + h_cost
            states.append((list_state, f_cost)) # cost: number of flips

    if len(states):
        states.pop(0) # removes the first state which is the same as the first state

    return states

def run_solver(start_state, goal_state, solver):
    """
    Should only contain the start state, the goal state, and the solver as input
    
    """
    Node.getNeighbors = _getNeighbors
    
    pancake_solver = solver
    pancake_solver.solve(start_state, goal_state)
    stats = pancake_solver.get_statistics()
    print(stats)
    