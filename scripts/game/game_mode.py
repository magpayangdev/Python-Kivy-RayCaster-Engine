""" game mode - is the game mode. 
	decides the map, player stats, sound themes and so on.... """

from settings import *
from kivy.clock import Clock
from scripts.modules.loaders import auto_loader_module as lsa

class GameMode:
	def __init__(self, window):
		self.mode = 0
		self.tick = None
		
		self.loop_num = -1
		self.kw_args = None
		self.do_once = True
		self.paused = False
		self.window = window

		self.wt = None
		self.hud = None
		self.sky = None
		self.menu = None
		self.event= None
		self.floor = None
		self.audio = None
		self.world = None
		self.player = None
		self.minimap = None
		self.tc_mngr = None
		self.l_screen = None
		self.game_mode = None
		self.graph_mngr = None
		self.primary_loop = None
		self.sprite_space = None
		
		self.start_loading()

	def re_init(self):
		if self.l_screen:
			self.l_screen.re_init()
			
	def start_loading(self):
		if self.event:
			self.event.start_loading()
			
		else:	
			lsa.re_init(self)
			lsa.create_loading_screen(self)
			self.tick = Clock.schedule_interval(lsa.update, 0)
