from typing import Dict, List
import numpy as np
from solver import Solver, Node, Graph
from utils import PriorityQueue

class RTAStar(Solver):
    """docstring for UCS"""
    def __init__(self):
        super().__init__()
        self.use_heuristic_cost = True

    def solve(self, start_state: List[int], goal_state: List[int]) -> int:
    	pass