#bfs
import collections
class graph:
	def __init__(self,gdict=None):
		if gdict is None:
			gdict = {}
		self.gdict = gdict

	def getVertices(self):
		return list(self.gdict.keys())
# Check for the visisted and unvisited nodes
def bfs(graph, startnode,goalnode):
	# Track the visited and unvisited nodes using queue
	seen, queue = set([startnode]), collections.deque([startnode])
	while queue:
		vertex = queue.popleft()
		marked(vertex)
		if vertex==goalnode:
			print("Goal node found at",vertex)
			exit(1)
		for node in graph[vertex]:
			if node not in seen:
				seen.add(node)
				queue.append(node)

def marked(n):
	print(n)

gdict = {}


n=int(input("Enter number of vertices:"))
for i in range(n):
    print("Enter vertice",i+1)
    x=input()
    st=set()
    print("Enter number of adjacent nodes for",x)
    n1=int(input())
    for j in range(n1):
        print("Enter adjacent node",j+1)
        str=input()
        st.add(str)
    gdict[x]=st

    
goal=input("Enter goal node:")
start=input("Enter starting node:")

print(gdict)

bfs(gdict,start,goal)
