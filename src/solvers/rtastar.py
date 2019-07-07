from typing import Dict, List
import numpy as np
from solver import Solver, Node, Graph
from utils import PriorityQueue

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
        pass
    	# openSet = PriorityQueue()
     #    closedSet = set()

     #    start_node = Node(start_state)
     #    goal_node = Node(goal_state)

     #    openSet.insert(start_node, 0, 0)

     #    self.cost = float('inf')

     #    self.cost_so_far[start_node.hash()] = 0
        
     #    while not openSet.is_empty():
     #        if self.cost <= openSet.peek():
     #            self.optimal_path = self.get_optimal_path(possible_goal)
     #            return

     #        current = openSet.remove()

     #        self.nodes_expanded += 1
            
     #        neighbors = current.getNeighbors(current.state, current.g, self.use_heuristic_cost, goal_node.state)

     #        if neighbors:
     #            for neighbor in neighbors:
     #                if neighbor.hash() in openSet.entry_finder and neighbor.g >= self.cost_so_far[neighbor.hash()]:
     #                    continue
                    
     #                if neighbor.hash() in closedSet:
     #                    continue
                    
     #                self.cost_so_far[neighbor.hash()] = neighbor.g
     #                self.graph.setParent(current, neighbor, neighbor.g)
        
     #                if neighbor.isGoal(goal_node) and neighbor.g < self.cost:
     #                    self.cost = neighbor.g
     #                    possible_goal = neighbor

     #                openSet.insert(neighbor, neighbor.g, neighbor.h)

     #        closedSet.add(current.hash())
