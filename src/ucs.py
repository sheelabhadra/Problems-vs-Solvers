import numpy as np
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
        def get_manhattan_cost(state):
            """ Computes Manhattan distance between 2 states
            Args:
                state (list[int]):
                goal_state (list[int]):
            Returns:
                manhattan_cost (int):
            """
            goal_state = state[:]
            goal_state.sort()
            goal_state.append(goal_state.pop(0))

            state_tile = np.reshape(state, (N, N))
            goal_state_tile = np.reshape(goal_state, (N, N))

            mahanttan_cost = 0
            for si in range(N):
                for sj in range(N):
                    for gi in range(N):
                        for gj in range(N):
                            if not state_tile[si][sj]:
                                continue
                            if state_tile[si][sj] == goal_state_tile[gi][gj]:
                                mahanttan_cost += abs(gi - si) + abs(gj - sj)

            return mahanttan_cost

        def swap(state, idx1, idx2):
            new_state = state[:]
            new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
            return new_state

        def add_state(state, state_cost):
            if str(state) not in dict_predecessors:
                states.append((state, state_cost))

        len_state, states = len(state), []
        N = int(np.sqrt(len_state))

        # gets the position of the blank cell
        blank_idx = state.index(0)

        left_state, right_state, up_state, down_state = [], [], [], []
        # get the next states
        if (blank_idx+1)%N: # not on the right edge
            # right
            right_state = swap(state, blank_idx, blank_idx+1)
            right_state_cost = get_manhattan_cost(right_state)

        if (blank_idx+1)//N: # not on the top edge           
            # up
            up_state = swap(state, blank_idx, blank_idx-N)
            up_state_cost = get_manhattan_cost(up_state)

        if (blank_idx+1)%N != 1: # not on the left edge
            # left 
            left_state = swap(state, blank_idx, blank_idx-1)
            left_state_cost = get_manhattan_cost(left_state)

        if (blank_idx+1)//N != N: # not on the bottom edge
            # down
            down_state = swap(state, blank_idx, blank_idx+N)
            down_state_cost = get_manhattan_cost(down_state)

        if len(left_state):
            add_state(left_state, left_state_cost)
        if len(right_state):
            add_state(right_state, right_state_cost)
        if len(up_state):
            add_state(up_state, up_state_cost)
        if len(down_state):
            add_state(down_state, down_state_cost)

        return states
        # len_state, states = len(state), []

        # for i in range(len_state):
        #     sub_list = state[0:i+1]
        #     len_sub_list = len(sub_list)

        #     tail_list = state[i+1:len_state]

        #     # flip the state
        #     sub_list = sub_list[::-1]

        #     # concatenate the two lists to obtain the new state
        #     list_state = sub_list + tail_list

        #     # insert the states and the edge cost if the state does not exist in dict_predecessors
        #     if str(list_state) not in dict_predecessors:
        #         states.append((list_state, i+1))

        # if len(states):
        #     states.pop(0) # removes the first state which is the same as the first state

        # return states


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

