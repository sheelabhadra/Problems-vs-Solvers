from problem import *
from ucs import *

# def get_states(state, goal_state, dict_predecessors):
#     def get_manhattan_cost(state, goal_state):
#         """ Computes Manhattan distance between 2 states
#         Args:
#             state (list[int]):
#             goal_state (list[int]):
#         Returns:
#             manhattan_cost (int):
#         """
#         state_tile = np.reshape(state, (N, N))
#         goal_state_tile = np.reshape(goal_state, (N, N))

#         mahanttan_cost = 0
#         for si in range(N):
#             for sj in range(N):
#                 for gi in range(N):
#                     for gj in range(N):
#                         if not state_tile[si][sj]:
#                             continue
#                         if state_tile[si][sj] == goal_state_tile[gi][gj]:
#                             mahanttan_cost += abs(gi - si) + abs(gj - sj)

#         return mahanttan_cost

#     def swap(state, idx1, idx2):
#         new_state = state[:]
#         new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
#         return new_state

#     def add_state(state, state_cost):
#         if str(state) not in dict_predecessors:
#             states.append((state, state_cost))

#     len_state, states = len(state), []
#     N = int(np.sqrt(len_state))

#     # gets the position of the blank cell
#     blank_idx = state.index(0)

#     left_state, right_state, up_state, down_state = [], [], [], []
#     # get the next states
#     if (blank_idx+1)%N: # not on the right edge
#         # right
#         right_state = swap(state, blank_idx, blank_idx+1)
#         right_state_cost = get_manhattan_cost(right_state, goal_state)

#     if (blank_idx+1)//N: # not on the top edge           
#         # up
#         up_state = swap(state, blank_idx, blank_idx-N)
#         up_state_cost = get_manhattan_cost(up_state, goal_state)

#     if (blank_idx+1)%N != 1: # not on the left edge
#         # left 
#         left_state = swap(state, blank_idx, blank_idx-1)
#         left_state_cost = get_manhattan_cost(left_state, goal_state)

#     if (blank_idx+1)//N != N: # not on the bottom edge
#         # down
#         down_state = swap(state, blank_idx, blank_idx+N)
#         down_state_cost = get_manhattan_cost(down_state, goal_state)

#     if len(left_state):
#         add_state(left_state, left_state_cost)
#     if len(right_state):
#         add_state(right_state, right_state_cost)
#     if len(up_state):
#         add_state(up_state, up_state_cost)
#     if len(down_state):
#         add_state(down_state, down_state_cost)

#     return states

def main(): 
    start_state = [1, 0, 3, 4, 2, 5, 7, 8, 6]

    ucs_solver = UCS()
    total_cost = ucs_solver.run(start_state)
    print(total_cost)
    

if __name__ == "__main__":
    main()


