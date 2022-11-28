
from settings import *
from scripts.bases.base import Base
from scripts.bases.window_objects.rect_base import RectBase
from scripts.bases.window_objects.textured_rect import TexturedRect
from scripts.bases.window_objects.text_base import TextBase
from scripts.bases.window_objects.button_base import ButtonBase


class TextFrame(Base):
	def __init__(self, game, window, hide=False, bg_color=(0.1,0.5,0.3,1), image_name="py.png", image_category="game", text=SAMPLE_TEXT, font_name="Modenine", halign='center', valign='middle', font_size=100, text_color=(0.5,0.3,0.1,1), padding_x=100, padding_y=100, button_bg=(0.5,0.3,0.1,1), button_text='Skip', button_font_name='AdventureRequest', button_font_size=40, button_t_color=(1,1,1,1), button_size=(250,100), button_pos=(0, 0)):
		super().__init__(game=game)
		
		self.window=None
		
		if window:
			self.window=window
		else:
			self.window = game.window
	
		self.background = RectBase(game=self.game, window=self.window, color=bg_color, size=self.window.size, pos=self.window.pos, hide=hide)
		
		self.frame_image = TexturedRect(game=self.game, window=self.window, image_name=image_name, image_category=image_category, color=(1,1,1,1), size=(100,100), pos=(0,0,), hide=hide)
	
		self.frame_text = TextBase(game=self.game, window=self.window, text=text, font_name=font_name, halign=halign, valign=valign, font_size=font_size,  text_color=text_color, text_size=(100,100), padding_x=padding_x, padding_y=padding_y)
		
		self.frame_button = ButtonBase(game=self.game, window=self.window, background_color=button_bg, hide=hide, text=button_text, font_name=button_font_name, font_size=button_font_size, text_color=button_t_color, size=button_size, pos=button_pos)
		
		size=0,0
		pos=0,0
		
		if self.window.width>self.window.height:
			size=self.window.height, self.window.height
			pos=self.window.width/2 - self.window.height/2, 0
		else:
			size=self.window.width, self.window.width
			pos=self.window.width/2-self.window.width/2
		
		self.frame_image.rect.size=size
		self.frame_image.rect.pos=pos
		
		self.frame_text.size=size
	
	#<----Button	
	@property
	def button_widget(self):
		return self.frame_button.button_widget

	@property
	def button_text(self):
		return self.frame_button.button_text
		
	@property
	def button_size(self):
		return self.frame_button.button_size
		
	@property
	def button_pos(self):
		return self.frame_button.button_pos
		
	#<----Setters
	@button_text.setter
	def button_text(self, value):
		self.frame_button.button_text = value

	@button_size.setter
	def button_size(self, value):
		self.frame_button.button_size = value

	@button_pos.setter
	def button_pos(self, value):
		self.frame_button.button_pos = value		
	
	#<----Image	
	@property
	def texture(self):
		return self.frame_image.texture
		
	@property
	def image_size(self):
		return self.frame_image.rect.size
		
	@property
	def image_pos(self):
		return self.frame_image.rect.pos
	
	#<----Text		
	@property
	def text(self):
		return self.frame_text.text
		
	@text.setter
	def text(self, value):
		self.frame_text.text = value

	#<----Window	
	@property
	def width(self):
		return self.window.width
		
	@property
	def height(self):
		return self.window.height
	
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)

	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		pass

	def show(self):
		self.background.show()
		self.frame_image.show()
		self.frame_text.show()
		self.frame_button.show()
			
	def hide(self):
		self.background.hide()
		self.frame_image.hide()
		self.frame_text.hide()
		self.frame_button.hide()
			
	def remove(self):
		self.background.remove()
		self.frame_image.remove()
		self.frame_text.remove()
		self.frame_button.remove()
		
		del(self.background)
		del(self.frame_image)
		del(self.frame_text)
		del(self.frame_button)



