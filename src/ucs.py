import numpy as np
from solver import PriorityQueue

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

################################################################
#
# TODO: Add backtracking feature to obtain the minimum cost path
#
################################################################

class UCS:
    def get_states(self):
        pass

    def get_optimal_path(self):
        pass

    def run(self, start_state):
        goal_state = start_state[:]
        goal_state.sort()
        goal_state.append(goal_state.pop(0))

        graph = Graph()

        # fringe of the graph is a priority queue
        fringe = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        fringe.insert((Node(start_state), 0), 0)

        while not fringe.is_empty():
            node, cost_node = fringe.remove()

            if node.getState() == goal_state:
                return cost_node

            neighbors = self.get_states(node.getState(), graph.getPredecessors(node))

            if neighbors:
                for neighbor in neighbors:
                    state_neighbor, cost_edge = neighbor # unpack the tuple (state, cost_edge)
                    neighbor_node = Node(state_neighbor)
                    graph.setParent(node, neighbor_node, cost_edge)
                    cumulative_cost = cost_node + cost_edge
                    fringe.insert((neighbor_node, cumulative_cost), cumulative_cost)

