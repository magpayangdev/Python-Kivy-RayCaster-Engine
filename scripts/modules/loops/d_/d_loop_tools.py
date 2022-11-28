from kivy.clock import Clock
from settings import *

game=None
_i_a_d = None

def re_init(game_ref):
	global game
	game=game_ref

def level_clean_up():
	game.sprite_space.delete_all_sprts()	
	
def kill_loop():
	game.accum_time = 0.0	
	game.paused = False	
	game.loop_num = MAX_NUMBER
	Clock.unschedule(game.tick)
	
def start_pre_loop():
	kill_loop()
	game.accum_time = 0.0	
	game.paused = False	
	game.loop_num = 0		
	game.tick = Clock.schedule_interval(game.pre_loop, 0)
	
def start_primary_loop():
	kill_loop()
	game.accum_time = 0.0	
	game.paused = False	
	game.loop_num = 1		
	game.tick = Clock.schedule_interval(game.primary_loop, 0)
	
def start_secondary_loop():
	kill_loop()
	game.accum_time = 0.0	
	game.paused = False	
	game.loop_num = 2		
	game.tick = Clock.schedule_interval(game.secondary_loop, 0)
