from typing import Dict, List
import numpy as np
from solver import Solver, Node, Graph
from utils import PriorityQueue

class AStar(Solver):
    """docstring for UCS"""
    def __init__(self):
        super().__init__()
        self.use_heuristic_cost = True
    
    def solve(self, start_state: List[int], goal_state: List[int]) -> int:
        # frontier of the graph is a priority queue
        frontier = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        start_node = Node(start_state)
        frontier.insert((start_node, start_node.g), start_node.g)

        while not frontier.is_empty():
            node, cost_node = frontier.remove()

            if node.getState() == goal_state:
                # save some stats here
                self.cost = cost_node
                self.optimal_path = self.get_optimal_path(node, goal_state)
                return

            neighbors = node.getNeighbors(node.getState(), self.graph.getPredecessors(node), self.use_heuristic_cost)

            if neighbors:
                for neighbor in neighbors:
                    state_neighbor, cost_edge = neighbor # unpack the tuple (state, cost_edge)
                    neighbor_node = Node(state_neighbor)
                    self.graph.setParent(node, neighbor_node, cost_edge)
                    cumulative_cost = cost_node + cost_edge
                    neighbor_node.g = cumulative_cost
                    frontier.insert((neighbor_node, cumulative_cost), cumulative_cost)
