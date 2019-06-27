from typing import Dict, List
import numpy as np
from solvers.solver import Solver, Node, Graph
from utils.utils import PriorityQueue
import itertools

"""
class UCS(Solver):
    def __init__(self):
        super().__init__()
    
    def solve(self, start_state, goal_state):
        # OPEN list: frontier (priority queue)
        # CLOSED list: self.cost_so_far
        # frontier of the graph is a priority queue
        frontier = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        start_node = Node(start_state)
        start_node.g, start_node.h = 0, 0
        frontier.insert(start_node, start_node.hash(), 0)
        self.cost_so_far[start_node.hash()] = 0

        while not frontier.is_empty():
            node = frontier.remove()
            self.nodes_expanded += 1

            if node.isGoal(goal_state):
                # save some stats here
                self.cost = self.cost_so_far[node.hash()]
                self.optimal_path = self.get_optimal_path(node)
                return

            neighbors = node.getNeighbors(node.state, self.graph.getPredecessors(node), self.use_heuristic_cost, goal_state)

            if neighbors:
                for neighbor in neighbors:
                    new_cost = self.cost_so_far[node.hash()] + 1
                    if (neighbor.hash() not in self.cost_so_far) or (new_cost < self.cost_so_far[neighbor.hash()]):
                        self.cost_so_far[neighbor.hash()] = new_cost
                        self.graph.setParent(node, neighbor, neighbor.g)
                        priority = new_cost + neighbor.h # new_cost: priority
                        frontier.insert(neighbor, neighbor.hash(), priority)

"""

""" Strategy suggested by Dr. Sharon
Perform the goal test when generating a node.
If goal==true then store the node.
once the best f-value in the open list is smaller or equal to the stored node f-value then you can stop and return the stored node as goal.
"""

"""
class UCS(Solver):
    def __init__(self):
        super().__init__()
    
    def solve(self, start_state, goal_state):
        # OPEN list: frontier (priority queue)
        # CLOSED list: self.cost_so_far
        # frontier of the graph is a priority queue
        open_list = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        start_node = Node(start_state)
        goal_node = Node(goal_state)

        open_list.insert(start_node, 0)
        self.cost_so_far[start_node.hash()] = 0

        while not open_list.is_empty():
            node = open_list.remove()
            self.nodes_expanded += 1

            if node.isGoal(goal_node):
                # save some stats here
                self.cost = self.cost_so_far[node.hash()]
                self.optimal_path = self.get_optimal_path(node)
                return

            neighbors = node.getNeighbors(node.state, self.graph.getPredecessors(node), self.use_heuristic_cost, goal_state)

            repeat_count = 0
            if neighbors:
                for neighbor in neighbors:
                    new_cost = self.cost_so_far[node.hash()] + 1
                    if (neighbor.hash() not in self.cost_so_far) or (new_cost < self.cost_so_far[neighbor.hash()]):
                        self.cost_so_far[neighbor.hash()] = new_cost
                        self.graph.setParent(node, neighbor, neighbor.g)
                        priority = new_cost + neighbor.h # new_cost: priority
                        repeat_count += 1
                        open_list.insert(neighbor, priority)
"""

"""
class UCS(Solver):
    def __init__(self):
        super().__init__()
    
    def solve(self, start_state, goal_state):
        # OPEN list: open_list
        # CLOSED list: self.cost_so_far
        # frontier of the graph is a priority queue
        openSet = PriorityQueue()
        closedSet = set()

        start_node = Node(start_state)
        goal_node = Node(goal_state)

        openSet.insert(start_node, 0)
        self.cost_so_far[start_node.hash()] = 0
        
        while not openSet.is_empty():
            current = openSet.remove()
            self.nodes_expanded += 1

            if current.isGoal(goal_node):
                self.cost = self.cost_so_far[current.hash()]
                self.optimal_path = self.get_optimal_path(current)
                return

            closedSet.add(current.hash())

            neighbors = current.getNeighbors(current.state, self.graph.getPredecessors(current), self.use_heuristic_cost, goal_node.state)
            if neighbors:
                for neighbor in neighbors:
                    new_cost = self.cost_so_far[current.hash()] + neighbor.g
                    if neighbor.hash() in closedSet and new_cost >= self.cost_so_far[neighbor.hash()]:
                        continue
                    if neighbor.hash() not in closedSet or new_cost < self.cost_so_far[neighbor.hash()]:
                        self.graph.setParent(current, neighbor, neighbor.g)
                        self.cost_so_far[neighbor.hash()] = new_cost
                        priority = new_cost + neighbor.h # new_cost: priority
                        if neighbor.hash() not in openSet.entry_finder:
                            openSet.insert(neighbor, priority)
"""

"""
class UCS(Solver):
    def __init__(self):
        super().__init__()
    
    def solve(self, start_state, goal_state):
        openSet = PriorityQueue()
        closedSet = set()

        start_node = Node(start_state)
        goal_node = Node(goal_state)

        openSet.insert(start_node, 0)
        self.cost_so_far[start_node.hash()] = 0
        
        while not openSet.is_empty():
            current = openSet.remove()
            self.nodes_expanded += 1

            if current.isGoal(goal_node):
                self.cost = self.cost_so_far[current.hash()]
                self.optimal_path = self.get_optimal_path(current)
                return

            neighbors = current.getNeighbors(current.state, self.cost_so_far[current.hash()], self.use_heuristic_cost, goal_node.state)
            
            if neighbors:
                for neighbor in neighbors:
                    if neighbor.hash() in openSet.entry_finder and self.cost_so_far[neighbor.hash()] <= neighbor.g:
                        continue
                    
                    elif neighbor.hash() in closedSet:
                        if self.cost_so_far[neighbor.hash()] <= neighbor.g:
                            continue
                        priority = neighbor.g + neighbor.h
                        closedSet.remove(neighbor.hash())
                        openSet.insert(neighbor, priority)
                    
                    else:
                        priority = neighbor.g + neighbor.h
                        openSet.insert(neighbor, priority)

                    self.cost_so_far[neighbor.hash()] = neighbor.g
                    self.graph.setParent(current, neighbor, neighbor.g)

                    # if neighbor.hash() in closedSet and neighbor.g >= self.cost_so_far[neighbor.hash()]:
                    #     continue
                    
                    # if neighbor.hash() not in closedSet or neighbor.g < self.cost_so_far[neighbor.hash()]:
                    #     self.graph.setParent(current, neighbor, neighbor.g)
                    #     self.cost_so_far[neighbor.hash()] = neighbor.g
                        
                    #     if neighbor.hash() not in openSet.entry_finder:
                    #         priority = neighbor.g + neighbor.h
                    #         openSet.insert(neighbor, priority)

            closedSet.add(current.hash())
"""

# Dr. Sharon's code

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
            print(openSet.peek())
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
        
                    if neighbor.isGoal(goal_node) and self.cost_so_far[neighbor.hash()] < self.cost:
                        self.cost = self.cost_so_far[neighbor.hash()]
                        possible_goal = neighbor

                    openSet.insert(neighbor, priority)

            closedSet.add(current.hash())
