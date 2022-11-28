
""" Used in plotting grid squares of maps 
		and in plotting sprites icon on minimaps """
from settings import *
	
_game=None
_graph_mngr=None
_graph=None

_world_width, _world_height = 0,0
_grid_width, _grid_height = 0,0

_grid_scale_x, _grid_scale_y = 0,0
_grid_scr_offset_x, _grid_scr_offset_y = 0,0

def init(game_ref, graph_ref):
	global _game, _graph_mngr, _graph
	global _world_width, _world_height
	global _grid_width, _grid_height
	global _grid_scale_x, _grid_scale_y
	global _grid_screen_offset_x, _grid_screen_offset_y
	
	_game = game_ref
	_graph = graph_ref
	
	_world_width, _world_height = _graph.world_width, _graph.world_height
	_grid_width, _grid_height = NUMBER_OF_BLOCKS_ACROSS, NUMBER_OF_BLOCKS_DOWN
	
	_grid_scale_x, _grid_scale_y = g_block_size()
	_grid_screen_offset_x, _grid_screen_offset_y = map_centre_o()
	
def world_to_grid_cells(world_x, world_y):
	ppx, ppy = _game.player.pos_x, _game.player.pos_y
	
	local_x, local_y = world_to_grid(world_x, world_y, ppx, ppy)
	
	return int(local_x), int(local_y)
	
def world_to_grid_index(world_x, world_y):
	ppx, ppy = _game.player.pos_x, _game.player.pos_y	
	
	local_x, local_y = world_to_grid(world_x, world_y, ppx, ppy)
	
	return int(local_x) + int(local_y) * grid_width

def grid_idx_to_grid(idx):
	col = idx % _grid_width
	row = idx // _grid_height
	return col, row
	
def grid_to_world(col, row, ppx, ppy):
	max_width = _world_width - _grid_width
	max_height = _world_height - _grid_height
	
	centre_x = ppx - _grid_width / 2
	centre_y = ppy - _grid_height / 2
	
	w_c = col + max(0, min(max_width, centre_x))
	w_r = row + max(0, min(max_height, centre_y))
	
	return w_c, w_r
	
def world_to_grid(world_x, world_y, ppx, ppy):	
	max_coord_x = _world_width - _grid_width
	max_coord_y = _world_height - _grid_height
	
	current_x = ppx - _grid_width / 2
	current_y = ppy - _grid_height / 2
	
	x = max(0, min(max_coord_x, current_x))
	y = max(0, min(max_coord_y, current_y))
	
	local_x = world_x - x
	local_y = world_y - y
	
	return local_x, local_y
	
def grid_to_screen(grid_x, grid_y):
	s_x = grid_x * _grid_scale_x + _grid_screen_offset_x
	s_y = (_grid_height - grid_y) * _grid_scale_y + _grid_screen_offset_y
	return s_x, s_y
	
def world_to_screen_player(ppx, ppy):
	g_x, g_y = world_to_grid(ppx, ppy, ppx, ppy)
	s_x, s_y = grid_to_screen(g_x - 0.5, g_y + 0.5)
	return s_x, s_y
	
def world_to_screen_sprite(world_x, world_y, ppx, ppy):
	g_x, g_y = world_to_grid(world_x, world_y, int(ppx) + 0.5, int(ppy) + 0.5)
	s_x, s_y = grid_to_screen(g_x - 0.5, g_y + 0.5)
	return s_x, s_y	

def world_to_screen(world_x, world_y, ppx, ppy):
	s_x, s_y = 0,0	
	return s_x, s_y		
	



