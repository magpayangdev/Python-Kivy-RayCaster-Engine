"""
hud
"""
import math
from settings import *
from scripts.modules.textures import * 
from scripts.modules.kivy.quadrant_manager import QManager
from scripts.screen_objects.hud_scripts.hit_rect import HitRect
from scripts.screen_objects.hud_scripts.hud_buttons import HudButtons
from scripts.screen_objects.hud_scripts.player_sprite import PlayerSprite
from scripts.screen_objects.hud_scripts.controller import LeftController, RightController
from scripts.screen_objects.hud_scripts.player_health_register import PlayerHealthRegister


class Hud(QManager):
	def __init__(self, game):
		super().__init__(game)
		#self.game.hud = self
		self.rst_hit_rect = False
		self.left_xypad_active = False
		self.right_xypad_active = False
		
		self.player_sprt = PlayerSprite(self.game)
		self.left_xypad = LeftController(self.game)
		self.right_xypad = RightController(self.game)
		self.player_health = PlayerHealthRegister(self.game)
		self.hud_buttons = HudButtons(self.game)
		self.hit_rect = HitRect(self.game)
		self.in_cnvs = False
	
	def re_init(self):
		pass
	
	def show(self):
		if not self.in_cnvs:
			self.player_sprt.show()
			self.hud_buttons.show()
			self.left_xypad.show()
			self.right_xypad.show()
			self.player_health.show()
			super().show()

	def hide(self):
		if self.in_cnvs:
			self.player_sprt.hide()
			self.hud_buttons.hide()
			self.left_xypad.hide()
			self.right_xypad.hide()
			self.player_health.hide()
			super().hide()
			
	def remove(self):
		if self.in_cnvs:
			self.hide()
		self.game.hud = None
		super.remove()			

	def update(self, dt):	
		super().update(dt)

	def fbf_update(self,dt):

		super().fbf_update(dt)
		
	def timed_update(self):
		self.player_health.flip()
		if self.rst_hit_rect:
			self.rst_hit_rect = False
			self.colour.rgba = 0,0,0,0	
		super().timed_update()	
	
	def game_over(self):
		self.hit_rect.colour.rgba = 1,1,1,1
		self.hit_rect.rect.texture = get_menu_texture('game_over.png')
		
	def victory(self):
		self.hit_rect.colour.rgba = 1,1,1,1
		self.hit_rect.rect.texture = get_menu_texture('victory.png')

	def player_is_hit(self):			
		self.accum_time = 0.0
		self.rst_hit_rect = True
		self.colour.rgba = 1,0,0,0.5

	#<---- Receive Touch Events	
	def on_touch_down(self, touch):			
		self.hud_buttons.on_touch_down(touch)
		super().on_touch_down(touch)
		
	def on_touch_move(self, touch):			
		self.hud_buttons.on_touch_move(touch)
		super().on_touch_move(touch)
		
	def on_touch_up(self, touch):				
		self.hud_buttons.on_touch_up(touch)
		super().on_touch_up(touch)				   	
	
	#<---- Touch Down Q1	
	def touch_down_q1(self, touch):
		super().touch_down_q1(touch)
		

		
	def touch_down_q2(self, touch):
		super().touch_down_q2(touch)
		pass
		
	def touch_down_q3(self, touch):


	def touch_down_q4(self, touch):
		super().touch_down_q4(touch)
		
	#<---- Touch Move Q1
	def touch_move_q1(self, touch):
		super().touch_move_q1(touch)

			
	def touch_move_q2(self, touch):
		super().touch_move_q2(touch)
		
	def touch_move_q3(self, touch):
		super().touch_move_q3(touch)

		
	def touch_move_q4(self, touch):
		super().touch_move_q4(touch)		

	#<---- Touch Up Q1
	def touch_up_q1(self, touch):
		super().touch_up_q1(touch)

			
	def touch_up_q2(self, touch):
		super().touch_up_q2(touch)
	
		
	def touch_up_q3(self, touch):
		super().touch_up_q3(touch)	

		
	def touch_up_q4(self, touch):
		super().touch_up_q4(touch)

								




			











