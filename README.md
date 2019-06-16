# Problems-vs-Solvers
Solving simple puzzles and games with solvers.  

## Games:
- [x] Pancake puzzle  
- [x] Tile puzzle

## Solvers:
- [x] Uniform Cost Search
- [x] A*

## Results
|Domain   |Solver   |Heuristic   |State Size   |Cost    | Expanded States  | Generated States  | CPU time (s)|
|:-------:|:-------:|:----------:|:-----------:|:------:|:----------------:|:-----------------:|:-----------:|
|pancake  |UCS      |None        |5            |3.47    |39.47             |74.53              | 0.003      |
|pancake  |A*       |Gap         |5            |3.47    |12.07             |34.33              | 0.001      |
|pancake  |UCS      |None        |6            |4.77    |295.67            |495.83             | 0.030      |
|pancake  |A*       |Gap         |6            |4.77    |29.13             |104.9              | 0.006      |
|pancake  |UCS      |None        |7            |5.40    |1435.93           |2831.3             | 0.200      |
|pancake  |A*       |Gap         |7            |5.40    |38.43             |181.73             | 0.007      |
|pancake  |UCS      |None        |8            |6.73    |16718.73          |26209.7            | 3.448      |
|pancake  |A*       |Gap         |8            |6.73    |140.20            |734.23             | 0.034      |
|pancake  |UCS      |None        |9            |7.80    |154436.53         |248379.53          | 58.212     |
|pancake  |A*       |Gap         |9            |7.80    |204.80            |1308.73            | 0.091      |
|pancake  |A*       |Gap         |10           |8.6     |325.17            |2428.23            | 0.114      |
|pancake  |A*       |Gap         |11           |9.73    |606.83            |4964.67            | 0.276      |
|pancake  |A*       |Gap         |12           |10.83   |1449.77           |13264.60           | 0.786      |
|tile     |UCS      |None        |3x3          |22      |90989.7           |109095.47          | 18.194     |
|tile     |A*       |Manhattan   |3x3          |22      |1128.83           |1712.33            | 0.583      |