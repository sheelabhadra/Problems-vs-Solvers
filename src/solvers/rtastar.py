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
        self.cost_table = {}

    def solve(self, start_state, goal_state) -> int:
        # No lookahead version
        start_node = Node(start_state)
        goal_node = Node(goal_state)

        self.cost = float('inf')
        current_node = start_node

        while not current_node.isGoal(goal_node):
            self.nodes_expanded += 1
            neighbors = current_node.getNeighbors(current_node.state, goal_node.state, self.use_heuristic_cost, current_node.g)

            if neighbors:
                f_min, min_neighbor = float('inf'), None
                idx, min_idx = 0, 0
                for neighbor in neighbors:
                    if neighbor.hash() in self.cost_table:
                        f = neighbor.g + self.cost_table[neighbor.hash()]
                    else:
                        f = neighbor.g + neighbor.h

                    if f < f_min:
                        f_min = f
                        min_neighbor = neighbor
                        min_idx = idx
                    idx += 1
                
                # Get the 2nd min
                neighbors.pop(min_idx)

                if neighbors:
                    f_min, min_neighbor_2 = float('inf'), None
                    for neighbor in neighbors:
                        if neighbor.hash() in self.cost_table:
                            f = neighbor.g + self.cost_table[neighbor.hash()]
                            # neighbor.h = cost_table[neighbor.hash()]
                        else:
                            f = neighbor.g + neighbor.h
                    
                        if f < f_min:
                            f_min = f
                            min_neighbor_2 = neighbor
                    
                self.cost_table[current_node.hash()] = f_min
                self.graph.setParent(current_node, min_neighbor)
                
                current_node = min_neighbor

        self.optimal_path = self.get_optimal_path(current_node)
        self.cost = self.nodes_expanded
