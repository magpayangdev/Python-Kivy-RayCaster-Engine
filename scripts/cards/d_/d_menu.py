
from scripts.bases.window_objects.rect_base import RectBase
from scripts.bases.window_objects.text_base import TextBase
from scripts.bases.window_objects.button_base import ButtonBase
from scripts.bases.window_objects.window_object import WindowObject

from settings import *

class Menu(WindowObject):
	def __init__(self, game, window, bg_color=(0.1,0.3,0.5,1), hide=False):
		super().__init__(game=game, window=window)
		
		self.background = RectBase(game=self.game, window=self.window, color=bg_color, size=self.window.size, pos=self.window.pos, hide=hide)

		self.title_text = TextBase(game=self.game, window=self.window, text='GAME TITLE', halign='center', valign='middle', font_name='AdventureRequest', font_size=200,  text_color=(1,1,1,1), text_size=(self.window.width,1000), padding_x=0, padding_y=0, hide=False)
		
		self.start_button = ButtonBase(game=self.game, window=self.window, hide=hide, text='START', background_color=(0,0,0,1), font_name='AdventureRequest', font_size=90, text_color=(1,1,1,1), size=(400,150), pos=(self.window.width/2,self.window.height/2 - 350))

	#<----Getters
	@property
	def width(self):
		return self.width
		
	@property
	def height(self):
		return self.height

	@property
	def button_widget(self):
		return self.start_button.button_widget

	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
		self.background.re_init()
		self.title_text.re_init()
		self.start_button.re_init()
				
	def update(self, dt):
		super().update(dt)
		self.background.update(dt)
		self.title_text.update(dt)
		self.start_button.update(dt)
			
	#<----Window Functions, re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
		self.background.show()
		self.title_text.show()
		self.start_button.show()
				
	def hide(self):
		super().hide()
		self.background.hide()
		self.title_text.hide()
		self.start_button.hide()
		
	def remove(self):
		super().remove()
		
		self.background.remove()
		self.title_text.remove()
		self.start_button.remove()
		
		del(self.background)
		del(self.title_text)
		del(self.start_button)
