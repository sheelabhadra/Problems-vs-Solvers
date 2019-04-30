from problem import Problem
from ucs import *

# class Pancake(Problem, Solver):
# 	super().__init__(initial, goal)
# 	self.initial_state = State(state)
# 	self.goal_state = State(goal)
# 	self.priority_queue = PriorityQueue()

# 	def numStates(self):
# 		return factorial(len(self.initial_state))

# 	def solve(self):
# 		pass

def get_states(state, dict_predecessors)
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


class PancakeUCS(UCS):
	def get_states(self, state, dict_predecessors):
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

	total_cost = ucs_solver.run(start_state)
	print(total_cost)
	

if __name__ == "__main__":
	main()

	