from typing import Dict, List
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

       
class Node:
    def __init__(self, state):
        self.state, self.parent = state, None

    def getState(self):
        return self.state

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent


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

    def get_states(self, *args, **kwargs):
        pass

    def get_optimal_path(self, node, goal_state: List[int]) -> List[List[int]]:
        path_dict = self.graph.getPredecessors(node)
        optimal_path = [goal_state]
        for key, state in path_dict.items():
            optimal_path.append(state)
        return optimal_path[::-1]

    def run(self, *args, **kwargs):
        pass