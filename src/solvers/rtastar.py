from typing import Dict, List
import numpy as np
from solvers.solver import Solver, Node, Graph
from utils.utils import PriorityQueue

"""
Goal: Reduce the execution time of A*
Method: Limit the search horizon of A* and select an action (single move) in constant time.
2 stages:
1. Make individual move decision: Perform mini-min search with alpha pruning
2. Make a sequence of decisions to arrive at a solution
	- recovering from inappropriate actions
	- avoid loops

Base strategy:
Backtrack to a previously visited state if

estimated cost of solving problem from that state + cost of returning to that state < 
estimated cost of solving problem from the current state

merit of a node n: f(n) = g(n) + h(n)
g(n): actual distance of the node n from the current state

store all visited nodes in a hash table with their "h" values

"""

class RTAStar(Solver):
    def __init__(self):
        super().__init__()

    def solve(self, start_state: List[int], goal_state: List[int]) -> int:
        # No lookahead version
        openSet = PriorityQueue()

        start_node = Node(start_state)
        goal_node = Node(goal_state)

        openSet.insert(start_node, 0, 0)
        self.cost = float('inf')

        cost_table = {}

        while not openSet.is_empty():
            if self.cost <= openSet.peek():
                self.optimal_path = self.get_optimal_path(possible_goal)
                return

            current = openSet.remove()
            self.nodes_expanded += 1
            # print(current.state)

            neighbors = current.getNeighbors(current.state, current.g, self.use_heuristic_cost, goal_node.state)

            if neighbors:
                f_min, min_neighbor = float('inf'), None
                idx, min_idx = 0, 0
                for neighbor in neighbors:
                    if neighbor.hash() not in self.cost_so_far:
                        self.cost_so_far[neighbor.hash()] = 1

                    if neighbor.hash() in cost_table:
                        f = neighbor.g + cost_table[neighbor.hash()]
                        neighbor.h = cost_table[neighbor.hash()]
                    else:
                        f = neighbor.g + neighbor.h
                    
                    # print(neighbor, " : ", f)

                    if f < f_min:
                        f_min = f
                        min_neighbor = neighbor
                        min_idx = idx
                    idx += 1
                
                if min_neighbor.isGoal(goal_node) and f_min < self.cost:
                    self.cost = f_min
                    possible_goal = min_neighbor

                openSet.insert(min_neighbor, min_neighbor.g, min_neighbor.h)

                # Get the 2nd min
                neighbors.pop(min_idx)

                if neighbors:
                    f_min, min_neighbor = float('inf'), None
                    for neighbor in neighbors:
                        if neighbor.hash() in cost_table:
                            f = neighbor.g + cost_table[neighbor.hash()]
                            neighbor.h = cost_table[neighbor.hash()]
                        else:
                            f = neighbor.g + neighbor.h
                    
                        if f < f_min:
                            f_min = f
                            min_neighbor = neighbor
                    
                    cost_table[current.hash()] = f_min


