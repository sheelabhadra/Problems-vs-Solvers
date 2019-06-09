import yaml
import domains.pancake as pancake
import domains.tile as tile
from solvers.ucs import *
from solvers.astar import *

# Read YAML file
with open("../config.yml", 'r') as stream:
    cfg = yaml.safe_load(stream)

for exp in cfg['EXPERIMENTS']:
    domain, start, goal, solver = eval(exp[0]), exp[1], exp[2], eval(exp[3])
    domain.run_solver(start, goal, solver)
