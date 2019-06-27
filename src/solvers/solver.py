from typing import Dict, List
from abc import abstractmethod

class Node:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    @abstractmethod
    def getNeighbors(self, *args, **kwargs):
        pass

    @abstractmethod
    def hash(self):
        pass

    def isGoal(self, goal):
        return self.hash() == goal.hash()

    def __eq__(self, other):
        return self.g == other.g

    def __lt__(self, other):
        return self.g < other.g

    def __gt__(self, other):
        return self.g > other.g

    def __repr__(self):
        return "%s" % (self.state)


class Graph:
    def setParent(self, source, destination, cost):
        destination.parent = source

    def getPredecessors(self, node):
        predecessors, current_parent = {}, node.parent
        while(current_parent):
            predecessors[current_parent.hash()] = current_parent.state
            current_parent = current_parent.parent
        return predecessors


class Solver:
    def __init__(self):
        self.graph = Graph()
        self.cost = float('inf')
        self.cost_so_far = {}
        self.optimal_path = None
        self.use_heuristic_cost = None
        self.nodes_expanded = 0

    def get_optimal_path(self, node):
        path_dict = self.graph.getPredecessors(node)
        optimal_path = [node.state]
        for key, state in path_dict.items():
            optimal_path.append(state)
        return optimal_path[::-1]

    @abstractmethod
    def solve(self, *args, **kwargs):
        pass

    def get_statistics(self):
        # minimum cost, optimal path
        stats = {'Cost': self.cost, 'Expanded_count': self.nodes_expanded, 'Generated_count': len(self.cost_so_far)}
        return stats

