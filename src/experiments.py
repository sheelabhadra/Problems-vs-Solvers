import yaml
import csv
import domains.pancake as pancake
import domains.tile as tile
from solvers.ucs import *
from solvers.astar import *

# Read YAML file
with open("../config.yml", 'r') as stream:
    cfg = yaml.safe_load(stream)

with open('experiment_stats.csv', mode='w') as csv_file:
    fieldnames = ['Domain', 'Solver', 'Heuristic', 'Cost', 'Optimal_path']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for exp in cfg['EXPERIMENTS']:
        domain, start, goal, solver, heuristic = eval(exp[0]), exp[1], exp[2], eval(exp[3]), exp[4]
        stats = domain.run_solver(start, goal, solver, heuristic)
        stats['Domain'], stats['Solver'], stats['Heuristic'] = exp[0], exp[3][:-2], exp[4]
        writer.writerow(stats)