# Searches

This project contain four different pathfinding algorithms: A* (A-star), Best-First Search, Depth-First Search (DFS), and Breadth-First Search (BFS). These algorithms are commonly used in finding optimal paths in graphs or grids. This readme provides an overview of each algorithm and their implementation within this project.

## Informed search algorithm

1. A* (A-star)
A* is a popular informed search algorithm that uses heuristics to find the optimal path between two points in a graph. It combines the cost to reach a node (the actual path cost) and an estimate of the remaining cost (heuristic) to guide the search. A* expands nodes with the lowest combined cost, thus finding the shortest path efficiently.

2. Best-First Search
Best-First Search is another informed search algorithm that prioritizes expanding nodes based on a heuristic function alone. It selects the most promising node according to the heuristic and explores in the direction that appears to lead closer to the goal. However, unlike A*, Best-First Search does not consider the actual path cost and may not always find the optimal path.

## Uninformed Search
3. Depth-First Search (DFS)
DFS is an uninformed search algorithm that explores as far as possible along each branch before backtracking. It traverses deeper into the graph or grid structure, often following a single branch until it reaches a dead-end before backtracking. DFS is not guaranteed to find the shortest path and can get trapped in infinite loops in certain cases.

4. Breadth-First Search (BFS)
BFS is an uninformed search algorithm that explores all the neighbors of a node before moving on to their neighbors. It visits nodes in layers, expanding the search from the starting node outward. BFS guarantees finding the shortest path in terms of the number of edges traversed but may not be the most efficient for large graphs or grids.
