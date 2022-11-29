
from scripts.bases.window_objects.text_base import TextBase
from scripts.bases.window_objects.rect_base import RectBase
from scripts.bases.window_objects.window_object import WindowObject


class LoadingScreen(WindowObject):
	""" Does not inherit from Card to make loading times faster """
	def __init__(self, game, window=None, **kwargs):
		super().__init__(game=game, window=window)
		
		color = kwargs.get('color')
		font_size = kwargs.get('font_size')
	
		self.rect_comp = RectBase(game=game, window=window, color=color, size=self.window.size, pos=self.window.pos, hide=False)
		
		self.text_comp = TextBase(game=game, window=window, text='', font_size = font_size)
		
	#<----Getters
	@property
	def width(self):
		return self.window.width
		
	@property
	def height(self):
		return self.window.height
		
	@property
	def text(self):
		return self.text_comp.text

	#<----Setter		
	@text.setter
	def text(self, value):
		self.text_comp.text = value
			
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
		
		self.rect_comp.size = self.window.size
		self.rect_comp.pos = self.window.pos
		
		#self.rect_comp.re_init()
		self.text_comp.re_init()
				
	def update(self, dt):
		super().update(dt)
		
		self.rect_comp.update(dt)
		self.text_comp.update(dt)
			
	#<----Window Functions, re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
		self.rect_comp.re_size()
		self.text_comp.re_size()
		
	def show(self):
		super().show()
		
		self.rect_comp.show()
		self.text_comp.show()
				
	def hide(self):
		super().hide()
		
		self.rect_comp.hide()
		self.text_comp.hide()
		
	def remove(self):
		super().remove()
		
		self.rect_comp.remove()
		self.text_comp.remove()
		
		del(self.rect_comp)
		del(self.text_comp)
		
		
		

