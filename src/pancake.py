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


def main(): 
	start_state = [1, 2, 4, 3]
	ucs_solver = UCS()
	total_cost = ucs_solver.run(start_state)
	print(total_cost)
	

if __name__ == "__main__":
	main()

	