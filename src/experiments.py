import yaml
import csv
import numpy as np
from timeit import default_timer as timer
import domains.pancake as pancake
import domains.tile as tile
from solvers.ucs import *
from solvers.astar import *
from solvers.rtastar import *
from solvers.lrtastar import *

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
            arr = [x for x in range(1, limit)]
            arr.append(0)
        
        scenarios_str = set([])
        scenarios = []
        num_scenarios = cfg['NUM_TRIALS']
        while len(scenarios) < num_scenarios:
            sc = list(np.random.permutation(arr))
            if sc == arr:
                continue
            if str(sc) not in scenarios_str:
                if cfg['DOMAIN']['NAME'] == "tile":
                    if tile.is_solvable(sc):
                        scenarios_str.add(str(sc))
                        scenarios.append(sc)
                elif cfg['DOMAIN']['NAME'] == "pancake":
                    # stats = pancake.run_solver(sc, sorted(sc), AStar(), "gap")
                    # if stats['Cost'] == 4:
                    scenarios_str.add(str(sc))
                    scenarios.append(sc)
        # print(tile.is_solvable([15,2,1,12,8,5,6,11,4,9,10,7,3,14,3,0]))
        # scenarios = [[1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15]]
        # scenarios = [[15,2,1,12,8,5,6,11,4,9,10,7,3,14,3,0]]
        # scenarios = [[1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15]]
        # print(scenarios)
        # scenarios = [[2,4,3,1]]
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
                # print("Done!" , cpu_time)

            stats['CPU_time'] = cpu_time/num_scenarios
            stats['Generated_count'] = generated/num_scenarios
            stats['Expanded_count'] = expanded/num_scenarios
            stats['Cost'] = cost/num_scenarios
            stats['Domain'], stats['Solver'], stats['Heuristic'] = cfg['DOMAIN']['NAME'], sol['NAME'][:-2], sol['HEURISTIC']
            stats['Len_state'] = len(arr)
            writer.writerow(stats)
            print("State size: {} Solver: {} completed!".format(limit, sol['NAME'][:-2], ))
