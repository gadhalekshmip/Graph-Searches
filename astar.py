def a_star(graph, start, goal, heuristic, path=[], path_cost=0):
    path = path + [start]
    if start == goal:
        return path, path_cost
    if start not in graph:
        return None
    min_path = None
    min_cost = float('inf')
    for neighbor, cost in graph[start]:
        if neighbor not in path:
            estimated_cost = path_cost + cost + heuristic[neighbor]
            if path_cost != 0:
                estimated_cost -= heuristic[path[-1]]
            new_path, new_cost = a_star(graph, neighbor, goal, heuristic, path, path_cost + cost)
            if new_path and new_cost < min_cost:
                min_path = new_path
                min_cost = new_cost
    if min_path:
        return min_path, min_cost
    else:
        # Backtrack
        for neighbor, cost in graph[start]:
            if neighbor in path:
                estimated_cost = path_cost + cost + heuristic[neighbor]
                if path_cost != 0:
                    estimated_cost -= heuristic[path[-1]]
                new_path, new_cost = a_star(graph, neighbor, goal, heuristic, path, path_cost + cost)
                if new_path and new_cost < min_cost:
                    min_path = new_path
                    min_cost = new_cost
        return min_path, min_cost
graph={}
heuristics={}
pcs={}
vertices=input("Enter the vertices: ")
vertices=vertices.split(" ")
for v in vertices:
	print("Enter the edges of {}".format(v))
	edges=input()
	if len(edges)==0:
		graph[v]=""
		continue
	edges=edges.split(" ")
	temp=[]
	for e in edges:
		print("Enter the pathcost from {} to {}".format(v,e))
		pc=float(input())
		temp.append((e,pc))
	graph[v]=temp
		#pcs[(v+e)]=pc

for node in graph:
	print("Enter the heuristic value of {}".format(node))
	h=int(input())
	heuristics[node]=h


start=input("enter the start node:")
goal=input("enter the goal node:")
path,path_cost = a_star(graph, start, goal, heuristics)

if path is not None:
    print("The path from {} to {} is: {}".format(start, goal, path))
    print("The cost of the path is: {}".format(path_cost))
else:
    print("There is no path from {} to {}".format(start, goal))
""" 

OUTPUT

Enter the vertices: 'S' 'A' 'B' 'C' 'D' 'E'
Enter the edges of 'S'
'A' 'B'
Enter the pathcost from 'S' to 'A'
1
Enter the pathcost from 'S' to 'B'
2
Enter the edges of 'A'
'C'
Enter the pathcost from 'A' to 'C'
3
Enter the edges of 'B'
'E'
Enter the pathcost from 'B' to 'E'
4
Enter the edges of 'C'
'D'
Enter the pathcost from 'C' to 'D'
5
Enter the edges of 'D'

Enter the edges of 'E'
'D'
Enter the pathcost from 'E' to 'D'
6
Enter the heuristic value of 'S'
6
Enter the heuristic value of 'A'
5
Enter the heuristic value of 'B'
4
Enter the heuristic value of 'C'
3
Enter the heuristic value of 'D'
0
Enter the heuristic value of 'E'
2
enter the start node:'S'
enter the goal node:'D'
The path from 'S' to 'D' is: ["'S'", "'A'", "'C'", "'D'"]
The cost of the path is: 9.0
"""