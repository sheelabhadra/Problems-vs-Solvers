from typing import Dict, List
from ucs import *
from solver import *
import timeit
import yaml

# # Read YAML file
# with open("../config.yml", 'r') as stream:
#     cfg = yaml.safe_load(stream)

def _getNeighborsHeuristic(self, state: List[int], dict_predecessors: Dict[str, List]) -> List[List[int]]:
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
        # if str(list_state) not in dict_predecessors:
        #     states.append((list_state, i+1)) # cost: number of pancakes flipped
        
        if str(list_state) not in dict_predecessors:
            g_cost = 1
            h_cost = 0
            f_cost = g_cost + h_cost
            states.append((list_state, g_cost)) # cost: number of flips

    if len(states):
        states.pop(0) # removes the first state which is the same as the first state

    return states

def _getNeighborsActual(self, state: List[int], dict_predecessors: Dict[str, List]) -> List[List[int]]:
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
        # if str(list_state) not in dict_predecessors:
        #     states.append((list_state, i+1)) # cost: number of pancakes flipped
        
        if str(list_state) not in dict_predecessors:
            g_cost = 1
            states.append((list_state, g_cost)) # cost: number of flips

    if len(states):
        states.pop(0) # removes the first state which is the same as the first state

    return states

def run_experiments(start_state, goal_state, solver):
    """
    Should only contain the start node and the goal node as input
    
    """
    pancake_solver = solver

    if pancake_solver.use_heuristic_cost:
        Node.getNeighbors = _getNeighborsHeuristic
    else:
        Node.getNeighbors = _getNeighborsActual

    pancake_solver.solve(start_state, goal_state)
    stats = pancake_solver.get_statistics()
    print(stats)


def main():
    start = [3,2,4,1] 
    goal = [1,2,3,4]
    run_experiments(start, goal, UCS())

if __name__ == "__main__":
    main()

# def main():
#     N = int(input("Enter the number of pancakes: "))
#     start_state = eval(input("Enter the start state (e.g. [1, 2, 3, 4] for N = 4): "))
#     while len(start_state) != N:
#         print("Number of pancakes is not ", N)
#         start_state = eval(input("Re-enter the start state (e.g. [1, 2, 3, 4] for N = 4): "))

#     goal_state = start_state[:]
#     goal_state.sort()

#     ucs_solver = UCS()
#     ucs_solver.get_states = _get_states
#     start = timeit.default_timer()
#     total_cost, optimal_path = ucs_solver.run(start_state, goal_state)
#     stop = timeit.default_timer()
#     print("Optimal sequence of states (Start State -> Intermediate States -> Goal State):\n", optimal_path)
#     print("Minimum Cost: ", total_cost)
#     print("Elapsed time: {0:.4f} secs".format(stop - start))


