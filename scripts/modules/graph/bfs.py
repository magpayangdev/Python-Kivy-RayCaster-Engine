
from collections import deque

_game=None
_graph_mngr=None
def init(game, graph):
	global _game, _graph_mngr
	_game = game
	_graph_mngr = graph

#<---- Algorithms:
def bfs(start, goal):	
	start = tuple(int(i) for i in start)
	goal = tuple(int(i) for i in goal)
	queue = deque([start])
	visited = {start: None}
				
	while queue:
		cur_node = queue.popleft()
		next_nodes = _graph_mngr.get_adjacent_nodes(cur_node)
				
		for next_node in next_nodes:
			if next_node not in visited and next_node not in _graph_mngr.npc_locs:
				queue.append(next_node)
				visited[next_node] = cur_node
							
			if next_node == goal:
				break
									
	return visited