from typing import Dict, List
import numpy as np
from solvers.solver import Solver, Node, Graph

class LRTAStar(Solver):
    def __init__(self):
        super().__init__()
        self.cost_table = {}

    def solve(self, start_state, goal_state):
        # No lookahead version
        start_node = Node(start_state)
        goal_node = Node(goal_state)

        queue = []

        while True:
            self.nodes_expanded = 0
            self.cost = float('inf')
            current_node = start_node

            while not current_node.isGoal(goal_node):
                self.nodes_expanded += 1

                neighbors = current_node.getNeighbors(current_node.state, goal_node.state, self.use_heuristic_cost)
                current_node.h = float('inf')

                if neighbors:
                    for neighbor in neighbors:
                        if neighbor.hash() in self.cost_table:
                            neighbor_f = neighbor.g + self.cost_table[neighbor.hash()]
                        else:
                            neighbor_f = neighbor.g + neighbor.h

                        if neighbor_f < current_node.h:
                            current_node.h = neighbor_f
                            next_node = neighbor
                    
                    self.cost_table[current_node.hash()] = current_node.h
                    self.graph.setParent(current_node, next_node)

                    current_node = next_node

            self.optimal_path = self.get_optimal_path(current_node)
            self.cost = self.nodes_expanded
            queue.append(self.cost)

            if len(queue) >= 10:
                last = queue[-10:]
                if len(set(last)) == 1:
                    return
