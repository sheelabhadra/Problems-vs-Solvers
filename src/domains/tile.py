from typing import Dict, List
from solvers.solver import Solver, Node, Graph
from solvers.ucs import *
from solvers.astar import *
from solvers.rtastar import *
from solvers.lrtastar import *
import timeit

def manhattan_heuristic(state, goal_state):
    """Calculates the Manhattan distance between the given state and the goal state
        
    Args:
        state: The given state

    Returns:
        manhattan_cost: The Manhattan distance

    """
    N = int(np.sqrt(len(state)))
    state_tile = np.reshape(state, (N, N))
    goal_state_tile = np.reshape(goal_state, (N, N))

    manhattan_cost = 0
    for si in range(N):
        for sj in range(N):
            for gi in range(N):
                for gj in range(N):
                    if not state_tile[si][sj]:
                        continue
                    if state_tile[si][sj] == goal_state_tile[gi][gj]:
                        manhattan_cost += abs(gi - si) + abs(gj - sj)

    return manhattan_cost


def euclidean_heuristic(state, goal_state):
    """Calculates the Euclidean distance between the given state and the goal state
        
    Args:
        state: The given state

    Returns:
        manhattan_cost: The Euclidean distance

    """
    N = int(np.sqrt(len(state)))
    state_tile = np.reshape(state, (N, N))
    goal_state_tile = np.reshape(goal_state, (N, N))

    euclidean_cost = 0
    for si in range(N):
        for sj in range(N):
            for gi in range(N):
                for gj in range(N):
                    if not state_tile[si][sj]:
                        continue
                    if state_tile[si][sj] == goal_state_tile[gi][gj]:
                        euclidean_cost += np.sqrt((gi - si)**2 + (gj - sj)**2)

    return euclidean_cost


def _hash(self):
    return str(self.state)


def _getNeighbors(self, state, goal_state, use_heuristic_cost, state_cost=0):
    """Gets the neighbor states (next states of child nodes) of the given state

    Args:
        state: The given state
        dict_predecessors: A dictionary containing the parents of the given state

    Returns:
        states: The neighbor states

    """

    def swap(state: List[int], idx1: int, idx2: int) -> List[int]:
        """Swaps two elements in a list given the indices of the elements

        Args:
            state: The given state
            idx1: The first index
            idx2: The second index

        Returns:
            new_state: The state after swapping the elements

        """
        new_state = state[:]
        new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
        return new_state


    len_state, states = len(state), []
    N = int(np.sqrt(len_state))

    # gets the position of the blank cell
    blank_idx = state.index(0)

    # get the next states
    left_state, right_state, up_state, down_state = [], [], [], [] # initialize the possible states as empty states
    
    if (blank_idx)%N != (N-1): # not on the right edge
        # right
        right_state = swap(state, blank_idx, blank_idx+1)
        
        g_cost_right = state_cost + 1
        if use_heuristic_cost == "manhattan":
            h_cost_right = manhattan_heuristic(right_state, goal_state)
        elif use_heuristic_cost == "euclidean":
            h_cost_right = euclidean_heuristic(right_state, goal_state)
        else:
            h_cost_right = 0
        f_cost_right = g_cost_right + h_cost_right

    if (blank_idx)//N: # not on the top edge           
        # up
        up_state = swap(state, blank_idx, blank_idx-N)
        
        g_cost_up = state_cost + 1
        if use_heuristic_cost == "manhattan":
            h_cost_up = manhattan_heuristic(up_state, goal_state)
        elif use_heuristic_cost == "euclidean":
            h_cost_up = euclidean_heuristic(up_state, goal_state)
        else:
            h_cost_up = 0
        f_cost_up = g_cost_up + h_cost_up

    if (blank_idx)%N: # not on the left edge
        # left 
        left_state = swap(state, blank_idx, blank_idx-1)
        
        g_cost_left = state_cost + 1
        if use_heuristic_cost == "manhattan":
            h_cost_left = manhattan_heuristic(left_state, goal_state)
        elif use_heuristic_cost == "euclidean":
            h_cost_left = euclidean_heuristic(left_state, goal_state)
        else:
            h_cost_left = 0
        f_cost_left = g_cost_left + h_cost_left

    if (blank_idx)//N != (N-1): # not on the bottom edge
        # down
        down_state = swap(state, blank_idx, blank_idx+N)
        
        g_cost_down = state_cost + 1
        if use_heuristic_cost == "manhattan":
            h_cost_down = manhattan_heuristic(down_state, goal_state)
        elif use_heuristic_cost == "euclidean":
            h_cost_down = euclidean_heuristic(down_state, goal_state)
        else:
            h_cost_down = 0
        f_cost_down = g_cost_down + h_cost_down

    # add the possible neighbor states
    if left_state:
        left_state = Node(left_state)
        left_state.g, left_state.h = g_cost_left, h_cost_left
        states.append(left_state)
    if right_state:
        right_state = Node(right_state)
        right_state.g, right_state.h = g_cost_right, h_cost_right
        states.append(right_state)
    if up_state:
        up_state = Node(up_state)
        up_state.g, up_state.h = g_cost_up, h_cost_up
        states.append(up_state)
    if down_state:
        down_state = Node(down_state)
        down_state.g, down_state.h = g_cost_down, h_cost_down
        states.append(down_state)
    return states

def is_solvable(start_state: List[int]) -> bool:
    """Checks solvability by counting the number of inversions of the start state.
    Can be optimized using merge sort.
    Link: http://www.cs.princeton.edu/courses/archive/spr18/cos226/assignments/8puzzle/index.html
    
    Args:
        start_state: The start state or initial configuration of the tile

    Returns:
        True if solvable, False otherwise

    """
    N = np.sqrt(len(start_state))
    start_state_cpy = start_state[:]
    blank_idx = start_state_cpy.index(0)
    blank_row = blank_idx//N

    start_state_cpy.pop(blank_idx)

    num_inversions = 0
    for i in range(len(start_state_cpy)):
        for j in range(i+1, len(start_state_cpy)):
            if start_state_cpy[i] > start_state_cpy[j]:
                num_inversions += 1
    
    # N - odd case
    if N%2:
        if not num_inversions%2:
            return True

    # N - even case
    else:
        if (num_inversions + blank_row)%2:
            return True

    return False


def run_solver(start_state, goal_state, solver, heuristic):
    """
    Should only contain the start node and the goal node as input
    
    """
    Node.getNeighbors = _getNeighbors
    Node.hash = _hash
    
    tile_solver = solver
    tile_solver.use_heuristic_cost = heuristic
    tile_solver.solve(start_state, goal_state)
    stats = tile_solver.get_statistics()
    return stats
