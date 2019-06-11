from typing import Dict, List
import numpy as np
from solvers.solver import Solver, Node, Graph
from utils.utils import PriorityQueue

class UCS(Solver):
    """docstring for UCS"""
    def __init__(self):
        super().__init__()
    
    def solve(self, start_state, goal_state):
        # frontier of the graph is a priority queue
        frontier = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        start_node = Node(start_state)
        start_node.g, start_node.h = 0, 0
        frontier.insert(start_node, start_node.hash(), 0)
        self.cost_so_far[start_node.hash()] = 0

        while not frontier.is_empty():
            node = frontier.remove()

            if node.isGoal(goal_state):
                # save some stats here
                self.cost = self.cost_so_far[node.hash()]
                self.optimal_path = self.get_optimal_path(node, goal_state)
                return

            neighbors = node.getNeighbors(node.state, self.graph.getPredecessors(node), self.use_heuristic_cost, goal_state)

            if neighbors:
                for neighbor in neighbors:
                    new_cost = self.cost_so_far[node.hash()] + neighbor.g
                    if (neighbor.hash() not in self.cost_so_far) or (new_cost < self.cost_so_far[neighbor.hash()]):
                        self.cost_so_far[neighbor.hash()] = new_cost
                        self.graph.setParent(node, neighbor, neighbor.g)
                        priority = new_cost # new_cost: priority
                        frontier.insert(neighbor, neighbor.hash(), priority)
                        