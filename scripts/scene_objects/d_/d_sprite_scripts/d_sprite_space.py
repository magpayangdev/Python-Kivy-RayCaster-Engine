""" sprite handler """
import random

#from kivy.uix.layout import Layout
from scripts.kivy_tools.base_layout import SpritesLayout
from scripts.scene_objects.sprite_scripts.sprite import *

from scripts.scene_objects.sprite_scripts import sprite_manager

class SpriteSpace(SpritesLayout):
	def __init__(self, game, hide=False, **kwargs):	
		super().__init__(game, hide=hide, **kwargs)
		self.game.sprite_space = self
		
		self.c_t_s = None		
		self.FOV_s = []
		self.o_s = []
		self.load_list = []

		loader.init(self.load_list)						

		self.reload_sprites()


					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
