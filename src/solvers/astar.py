from typing import Dict, List
# import numpy as np
from solvers.ucs import *
# from solver import Solver, Node, Graph
# from utils import PriorityQueue

class AStar(UCS):
    """docstring for UCS"""
    def __init__(self):
        super().__init__()
        self.use_heuristic_cost = True
