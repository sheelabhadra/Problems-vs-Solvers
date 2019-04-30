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

class UCS:
    def __init__(self):
        self.graph = Graph()

    def get_states(self):
        pass

    def get_optimal_path(self, node, goal_state):
        path_dict = self.graph.getPredecessors(node)
        optimal_path = [goal_state]
        for key, state in path_dict.items():
            optimal_path.append(state)
        return optimal_path[::-1]

    def run(self, start_state, goal_state):
        # frontier of the graph is a priority queue
        frontier = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        frontier.insert((Node(start_state), 0), 0)

        while not frontier.is_empty():
            node, cost_node = frontier.remove()

            if node.getState() == goal_state:
                print("Optimal sequence of states:", self.get_optimal_path(node, goal_state))
                return cost_node

            neighbors = self.get_states(node.getState(), self.graph.getPredecessors(node))

            if neighbors:
                for neighbor in neighbors:
                    state_neighbor, cost_edge = neighbor # unpack the tuple (state, cost_edge)
                    neighbor_node = Node(state_neighbor)
                    self.graph.setParent(node, neighbor_node, cost_edge)
                    cumulative_cost = cost_node + cost_edge
                    frontier.insert((neighbor_node, cumulative_cost), cumulative_cost)

