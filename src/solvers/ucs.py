from typing import Dict, List
import numpy as np
from solvers.solver import Solver, Node, Graph
from utils.utils import PriorityQueue
import itertools

class UCS(Solver):
    def __init__(self):
        super().__init__()
    
    def solve(self, start_state, goal_state):
        openSet = PriorityQueue()
        closedSet = set()

        start_node = Node(start_state)
        goal_node = Node(goal_state)

        openSet.insert(start_node, 0)

        self.cost = float('inf')

        self.cost_so_far[start_node.hash()] = 0
        
        while not openSet.is_empty():
            if self.cost <= openSet.peek():
                self.optimal_path = self.get_optimal_path(possible_goal)
                return

            current = openSet.remove()

            self.nodes_expanded += 1
            
            neighbors = current.getNeighbors(current.state, current.g, self.use_heuristic_cost, goal_node.state)

            if neighbors:
                for neighbor in neighbors:
                    if neighbor.hash() in openSet.entry_finder and neighbor.g >= self.cost_so_far[neighbor.hash()]:
                        continue
                    
                    if neighbor.hash() in closedSet:
                        continue
                        
                    priority = neighbor.g + neighbor.h
                    
                    self.cost_so_far[neighbor.hash()] = neighbor.g
                    self.graph.setParent(current, neighbor, neighbor.g)
        
                    if neighbor.isGoal(goal_node) and neighbor.g < self.cost:
                        self.cost = neighbor.g
                        possible_goal = neighbor

                    openSet.insert(neighbor, priority)

            closedSet.add(current.hash())
