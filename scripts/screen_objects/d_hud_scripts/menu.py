"""
menu
"""
from settings import *
from kivy.uix.label import Label
from scripts.modules.kivy import rectangle_creator as RC
from scripts.modules.kivy import button_creator as BC
from scripts.modules.kivy import label_creator as LC
import scripts.modules.kwargs.menu_kwargs as m_kwargs


class Menu:
	def __init__(self, game, color=DARK_RED,text='Menu',font_name='AdventureRequest',text_size=100, hide=False):
		self.game = game
		self.game.menu = self
		self.window = self.game.window
		self.accum_time = 0
		self.label = None
		self.button = None	
		self.colour = None
		self.rect = None
		self.in_cnvs = False
		
		m_kwargs.re_init(self)
		self.in_cnvs,self.colour,self.rect=RC.basic_rect(self.window, color, self.window.size, self.window.pos)
		self.label = LC.basic_label(self.window, self.label, text, font_name, text_size)
		self.button = BC.create_basic_button(self.window, self.button, **m_kwargs._start_button_kwargs)
		
		if hide:
			self.hide()
		
	def update(self, dt):
		self.accum_time += dt
		
		if self.accum_time > 1:
			self.accum_time = 0

	def show(self):
		if not self.in_cnvs:
			self.in_cnvs = True
			self.window.canvas.add(self.colour)
			self.window.canvas.add(self.rect)
			self.window.add_widget(self.label)			
			self.button = BC.create_basic_button(self.window, self.button, **m_kwargs._start_button_kwargs)
		
	def hide(self):
		if self.in_cnvs:
			self.in_cnvs = False
			self.window.canvas.remove(self.colour)
			self.window.canvas.remove(self.rect)
			self.window.remove_widget(self.label)
			self.window.remove_widget(self.button)
			
	def remove(self):
		self.hide()
		self.game.menu = None

	def button_cb(self, *args):
		self.remove()
		self.game.event.show_intro()
		pass
		
	def on_touch_down(self, touch):
		if not self.game.has_finished_loading:
			return
			
		if self.button.collide_point(*touch.pos):
			self.button.state = "down"
		
	def on_touch_move(self, touch):
		pass
		
	def on_touch_up(self, touch):	
		if not self.game.has_finished_loading:
			return
	
		if self.button.collide_point(*touch.pos):
			self.button.state = "normal"
	
	
	
	