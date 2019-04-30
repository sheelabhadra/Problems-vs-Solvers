from ucs import *

def _get_states(state, dict_predecessors):
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
    start_state = [1, 2, 4, 3]

    ucs_solver = UCS()
    ucs_solver.get_states = _get_states
    total_cost = ucs_solver.run(start_state)
    print(total_cost)

if __name__ == "__main__":
    main()

    