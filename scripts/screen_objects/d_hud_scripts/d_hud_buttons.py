
from kivy.uix.label import Label
from kivy.core.image import Image
from kivy.uix.button import Button	

import scripts.modules.kivy.label_creator as LC
import scripts.modules.kivy.button_creator as BC
import scripts.modules.kivy.rectangle_creator as RC
import scripts.modules.kwargs.hud_kwargs as b_kwargs


class HudButtons:
	def __init__(self, game):
		self.game = game
		self.hud = self.game.hud
		self.window = self.game.window
		
		b_kwargs.init(self)

		self.debug_label = LC.positioned_label(self.window, None, **b_kwargs._debug_text_kwargs)	
		self.exit_button = BC.create_basic_button(self.window, None, **b_kwargs._exit_button)
		self.all = (self.debug_label, self.exit_button)
		
		self.in_cnvs = True
		
		if True:
			self.hide()
			
	def re_init(self):
		b_kwargs.init(self.game.hud)
		
		self.debug_label = LC.positioned_label(self.window,self.debug_label,**b_kwargs._debug_text_kwargs)	
		self.exit_button = BC.create_basic_button(self.window,self.exit_button,**b_kwargs._exit_button)
		self.all = (self.debug_label, self.exit_button)
		
	def show(self):
		if not self.in_cnvs:
			[self.window.add_widget(entry) for entry in self.all]
			self.in_cnvs = True
			
	def hide(self):
		if self.in_cnvs:
			[self.window.remove_widget(entry) for entry in self.all]
			self.in_cnvs = False
			
	def remove(self):
		if self.in_cnvs:
			self.hide()
			
	def on_touch_down(self, touch):
		"""
		if self.exit_button.collide_point(*touch.pos):
			self.exit_button.state = 'down'
			return True
		"""
		
		if self.exit_button.does_collide(touch):
			self.exit_button.state = 'down'
			9/0
			return True

	def on_touch_move(self, touch):
		return True
					
	def on_touch_up(self, touch):
		return True

	#<---- button callbacks
	def e_b_callback(self, *args):
		if self.exit_button.state == 'down':
			self.game.window.quit_game()
			
	def centre_button_callback(self, *args):
		return True
			
	def l_b_callback(self, *args):
		return True
			
	def r_b_callback(self, *args):
		return True

































