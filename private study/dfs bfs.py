#graph = [[],[2,3,4],[5,6],[],[7,8],[9,10],[],[11,12],[],[],[],[],[]]
graph = [[],[2,3],[4,5],[4,6],[2,3,5,7],[2,4,7],[3,7],[4,5,6]]
visited = list()
def dfs_cycle(graph, v, visited): #순환을 이용한 DFS
	visited.append(v)
	print(v, end = " ")
	for i in graph[v]:
		if i not in visited:
			dfs_cycle(graph, i, visited)

def dfs_stack(graph,v): #스택을 이용한 DFS
	visited = list()
	stack = list()
	stack.append(v)
	while len(stack) != 0:
		v = stack.pop()
		if v not in visited:
			visited.append(v)
			print(v, end = " ")
			for i in reversed(graph[v]):
				stack.append(i)


def bfs(graph, v): #큐를 이용한 BFS
	queue = list()
	visited = list()
	queue.append(v)
	while len(queue) != 0:
		v = queue.pop(0)
		if v not in visited:
			visited.append(v)
			print(v, end = " ")
			for i in graph[v]:
				queue.append(i)	

print("<순환 DFS를 실행한 결과>")
dfs_cycle(graph,1,visited)
print()
print("<스택 DFS를 실행한 결과>")
dfs_stack(graph,1)
print()
print("<큐 BFS를 실행한 결과>")
bfs(graph, 1)