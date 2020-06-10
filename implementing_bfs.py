example_graph={
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
## visiting list 
## queued list     Here i have to make 2 list .One is queue for FIFO .Here i will remove the first element in the list and then append the element at the end 
visited=[]
queue=[]


def bfs_implementing(visited, graph, node): 
	visited.append(node)
	queue.append(node)
	print(queue)
	while queue:
		element=queue.pop(0)
		print(element,end=" ")



		for nearest in graph[element]:
			if nearest not in visited:
				visited.append(nearest)
				queue.append(nearest)
				# print('the element which is not visited--->.',visited)












bfs_implementing(visited,example_graph,'A')