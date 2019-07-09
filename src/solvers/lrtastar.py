from typing import Dict, List
import numpy as np
from solvers.solver import Solver, Node, Graph
from utils.utils import PriorityQueue

class LRTAStar(Solver):
    def __init__(self):
        super().__init__()
