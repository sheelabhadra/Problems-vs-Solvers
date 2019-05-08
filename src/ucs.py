from typing import Dict, List
import numpy as np
from solver import Solver, Node, Graph, PriorityQueue

class UCS(Solver):
    """docstring for UCS"""
    def __init__(self):
        super().__init__()
    
    def solve(self, start_state: List[int], goal_state: List[int]) -> int:
        # frontier of the graph is a priority queue
        frontier = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        frontier.insert((Node(start_state), 0), 0)

        while not frontier.is_empty():
            node, cost_node = frontier.remove()

            if node.getState() == goal_state:
                # save some stats here
                self.cost = cost_node
                self.optimal_path = self.get_optimal_path(node, goal_state)
                return

            neighbors = node.getNeighbors(node.getState(), self.graph.getPredecessors(node))

            if neighbors:
                for neighbor in neighbors:
                    state_neighbor, cost_edge = neighbor # unpack the tuple (state, cost_edge)
                    neighbor_node = Node(state_neighbor)
                    self.graph.setParent(node, neighbor_node, cost_edge)
                    cumulative_cost = self.cost_node + cost_edge
                    frontier.insert((neighbor_node, cumulative_cost), cumulative_cost)
