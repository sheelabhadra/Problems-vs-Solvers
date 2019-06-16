import yaml
import csv
import numpy as np
from timeit import default_timer as timer
import domains.pancake as pancake
import domains.tile as tile
from solvers.ucs import *
from solvers.astar import *

# Read YAML file
with open("../config.yml", 'r') as stream:
    cfg = yaml.safe_load(stream)

with open(cfg['OUTPUT_PATH'], mode='a') as csv_file:
    fieldnames = ['Domain', 'Solver', 'Heuristic', 'Len_state', 'Cost', 'Expanded_count', 'Generated_count', 'CPU_time']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for limit in cfg['DOMAIN']['STATE_SIZE']:
        if cfg['DOMAIN']['NAME'] == "pancake":
            arr = [x for x in range(1, limit+1)]
        elif cfg['DOMAIN']['NAME'] == "tile":
            arr = [x for x in range(0, limit+1)]
        
        scenarios_str = set([])
        scenarios = []
        num_scenarios = cfg['NUM_TRIALS']
        while len(scenarios) < num_scenarios:
            sc = list(np.random.permutation(arr))
            if str(sc) not in scenarios_str:
                scenarios_str.add(str(sc))
                scenarios.append(sc)

        for sol in cfg['SOLVER']:
            cost, generated, expanded, cpu_time = 0, 0, 0, 0
            for sc in scenarios:
                domain, start, goal, solver, heuristic = eval(cfg['DOMAIN']['NAME']), sc, arr, eval(sol['NAME']), sol['HEURISTIC']
                start_time = timer()
                stats = domain.run_solver(start, goal, solver, heuristic)
                end_time = timer()
                cpu_time += (end_time - start_time)
                cost += stats['Cost']
                generated += stats['Generated_count']
                expanded += stats['Expanded_count']

            stats['CPU_time'] = cpu_time/num_scenarios
            stats['Generated_count'] = generated/num_scenarios
            stats['Expanded_count'] = expanded/num_scenarios
            stats['Cost'] = cost/num_scenarios
            stats['Domain'], stats['Solver'], stats['Heuristic'] = cfg['DOMAIN']['NAME'], sol['NAME'][:-2], sol['HEURISTIC']
            stats['Len_state'] = len(arr)
            writer.writerow(stats)
            print("State size: {} Solver: {} completed!".format(limit, sol['NAME'][:-2], ))
