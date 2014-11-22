from collections import deque

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def clone_graph(src):
	clone_map = {}
	queue = deque()
	queue.append(src)
	clone_node = str(src)
	clone_map[src] = [clone_node]

	while queue:
		node = queue.popleft()
		for neighbor in graph[node]:
			if clone_map.get(neighbor, None):
				clone_map[node].append(clone_map[neighbor])
			else:
				clone_node = str(neighbor)
				queue.append(neighbor)
				clone_map[neighbor] = [clone_node]
				clone_map[node].append(clone_node)

	return clone_node

if __name__ == '__main__':
	clone_graph('A')




