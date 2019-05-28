import yaml
import pancake, tile
from ucs import *
from astar import *

# Read YAML file
with open("../config.yml", 'r') as stream:
    cfg = yaml.safe_load(stream)

for exp in cfg['EXPERIMENTS']:
    domain, start, goal, solver = eval(exp[0]), exp[1], exp[2], eval(exp[3])
    domain.run_solver(start, goal, solver)
