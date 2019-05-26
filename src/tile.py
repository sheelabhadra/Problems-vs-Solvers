from typing import Dict, List
from ucs import *
from problem import *
import timeit

def _getNeighbors(self, state: List[int], dict_predecessors: Dict[str, List], use_heuristic_cost, goal_state: List[int]) -> List[List[int]]:
    """Gets the neighbor states (next states of child nodes) of the given state

    Args:
        state: The given state
        dict_predecessors: A dictionary containing the parents of the given state

    Returns:
        states: The neighbor states

    """
    def get_manhattan_cost(state):
        """Calculates the Manhattan distance between the given state and the goal state
        
        Args:
            state: The given state

        Returns:
            manhattan_cost: The Manhattan distance

        """
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

    def add_state(state: List[int], state_cost: int) -> List[List[int]]:
        """Adds a state to the list of states

        Args:
            state: The given state
            state_cost: The cumulative cost of the state

        Returns:
            states: List of states with the new state added to it

        """
        if str(state) not in dict_predecessors:
            states.append((state, state_cost))

    len_state, states = len(state), []
    N = int(np.sqrt(len_state))

    # gets the position of the blank cell
    blank_idx = state.index(0)

    # get the next states
    left_state, right_state, up_state, down_state = [], [], [], [] # initialize the possible states as empty states
    
    if (blank_idx)%N != (N-1): # not on the right edge
        # right
        right_state = swap(state, blank_idx, blank_idx+1)
        
        g_cost_right = 1
        if use_heuristic_cost:
            h_cost_right = get_manhattan_cost(right_state)
        else:
            h_cost_right = 0
        right_state_cost = g_cost_right + h_cost_right

    if (blank_idx)//N: # not on the top edge           
        # up
        up_state = swap(state, blank_idx, blank_idx-N)
        
        g_cost_up = 1
        if use_heuristic_cost:
            h_cost_up = get_manhattan_cost(up_state)
        else:
            h_cost_up = 0
        up_state_cost = g_cost_up + h_cost_up

    if (blank_idx)%N: # not on the left edge
        # left 
        left_state = swap(state, blank_idx, blank_idx-1)
        
        g_cost_left = 1
        if use_heuristic_cost:
            h_cost_left = get_manhattan_cost(left_state)
        else:
            h_cost_left = 0
        left_state_cost = g_cost_left + h_cost_left

    if (blank_idx)//N != (N-1): # not on the bottom edge
        # down
        down_state = swap(state, blank_idx, blank_idx+N)
        
        g_cost_down = 1
        if use_heuristic_cost:
            h_cost_down = get_manhattan_cost(down_state)
        else:
            h_cost_down = 0
        down_state_cost = g_cost_down + h_cost_down

    # add the possible neighbor states
    if left_state:
        add_state(left_state, left_state_cost)
    if right_state:
        add_state(right_state, right_state_cost)
    if up_state:
        add_state(up_state, up_state_cost)
    if down_state:
        add_state(down_state, down_state_cost)

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


def run_solver(start_state, goal_state, solver):
    """
    Should only contain the start node and the goal node as input
    
    """
    Node.getNeighbors = _getNeighbors
    
    ucs_solver = solver
    ucs_solver.solve(start_state, goal_state)
    stats = ucs_solver.get_statistics()
    print(stats)
