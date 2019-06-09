from typing import Dict, List
from abc import abstractmethod

class Node:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    def getState(self):
        return self.state

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    @abstractmethod
    def getNeighbors(self, *args, **kwargs):
        pass

    def getPathCost(self):
        pass

    def getHeuristicCost(self):
        return 0

    def getTotalCost(self):
        return self.g + self.h

    def __lt__(self, other):
        pass



class Graph:
    def setParent(self, source, destination, cost):
        destination.setParent(source)

    def getPredecessors(self, node):
        predecessors, current_parent = {}, node.getParent()
        while(current_parent):
            predecessors[str(current_parent.getState())] = current_parent.getState()
            current_parent = current_parent.getParent()
        return predecessors


class Solver:
    def __init__(self):
        self.graph = Graph()
        self.cost = float('inf')
        self.cost_so_far = {}
        self.optimal_path = None
        self.use_heuristic_cost = False

    def get_optimal_path(self, goal_node, goal_state: List[int]) -> List[List[int]]:
        path_dict = self.graph.getPredecessors(goal_node)
        optimal_path = [goal_state]
        for key, state in path_dict.items():
            optimal_path.append(state)
        return optimal_path[::-1]

    @abstractmethod
    def solve(self, *args, **kwargs):
        pass

    def get_statistics(self):
        # minimum cost, optimal path
        stats = {'cost': self.cost, 'optimal_path': self.optimal_path}
        return stats

