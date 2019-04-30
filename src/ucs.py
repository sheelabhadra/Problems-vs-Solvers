from solver import Solver, PriorityQueue
# from queue import PriorityQueue

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
    """docstring for UCS"""
    # def __init__(self, graph, start, goal):
        # super().__init__()
        # self.graph = graph

    def get_states(self, state, dict_predecessors):
        len_state, states = len(state), []

        for i in range(len_state):
            sub_list = state[0:i+1]
            len_sub_list = len(sub_list)

            tail_list = state[i+1:len_state]

            # flip the state
            sub_list = sub_list[::-1]

            # concatenate the two lists to obtain the new state
            list_state = sub_list + tail_list

            # insert the states and the edge cost if the state does not exist in dict_predecessors
            if str(list_state) not in dict_predecessors:
                states.append((list_state, i+1))

        if len(states):
            states.pop(0) # removes the first state which is the same as the first state

        return states


    def get_optimal_path(self):
        pass 


    def run(self, state):
        goal_state = state[:]
        goal_state.sort()
        graph = Graph()

        # fringe of the graph is a priority queue
        fringe = PriorityQueue()

        # each item is a tuple (node, cumulative_cost)
        fringe.insert((Node(state), 0), 0)

        while not fringe.is_empty():
            node, cost_node = fringe.remove()
            print(self.show_pretty_pancakes(node.getState()))

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

