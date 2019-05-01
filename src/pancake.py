from typing import Dict, List
from ucs import *
from problem import *
import timeit
import argparse

def _get_states(state: List[int], dict_predecessors: Dict[str, List]) -> int:
    """Gets the neighbor states (next states of child nodes) of the given state

    Args:
        state: The given state
        dict_predecessors: A dictionary containing the parents of the given state

    Returns:
        states: The neighbor states

    """
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
            states.append((list_state, i+1))

    if len(states):
        states.pop(0) # removes the first state which is the same as the first state

    return states

def main():
    N = int(input("Enter the number of pancakes: "))
    start_state = eval(input("Enter the start state (e.g. [1, 2, 3, 4] for N = 4): "))
    while len(start_state) != N:
        print("Number of pancakes is not ", N)
        start_state = eval(input("Re-enter the start state (e.g. [1, 2, 3, 4] for N = 4): "))

    goal_state = start_state[:]
    goal_state.sort()

    ucs_solver = UCS()
    ucs_solver.get_states = _get_states
    start = timeit.default_timer()
    total_cost, optimal_path = ucs_solver.run(start_state, goal_state)
    stop = timeit.default_timer()
    print("Optimal sequence of states (Start State -> Intermediate States -> Goal State):\n", optimal_path)
    print("Minimum Cost: ", total_cost)
    print("Elapsed time: {0:.4f} secs".format(stop - start))

if __name__ == "__main__":
    main()

    