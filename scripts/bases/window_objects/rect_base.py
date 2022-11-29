
from scripts.bases.window_objects.window_object import WindowObject
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle	
#from scripts.modules.textures import *

	
class RectBase(WindowObject):
	""" The base class for all objects that requires a color and rectangle instruction """
	def __init__(self, game, window, color=(1,1,1,1), size=(100,100), pos=(0,0), hide=False):
		super().__init__(game=game, window=window)
		
		self.init_color = color
		self.init_size = size
		self.init_pos = pos
		
		self.colour = None
		self.rect = None
		self.in_cnvs = False
		with self.window.canvas:
			self.colour = Color(rgba=self.init_color)
			self.rect = Rectangle(size=self.init_size, pos=self.init_pos, texture=None)
			self.in_cnvs = True
			
		if hide:
			self.window.canvas.remove(self.colour)
			self.window.canvas.remove(self.rect)
			self.in_cnvs = False
			
	#<----Getter	
	@property
	def texture(self):
		return self.rect.texture
					
	@property
	def color(self):
		return self.colour.rgba
			
	@property
	def size(self):
		return self.rect.size
		
	@property
	def pos(self):
		return self.rect.pos

	#<----Setter
	@texture.setter
	def texture(self, value):
		self.rect.texture = value

	@color.setter
	def color(self, value):
		self.colour.rgba = value

	@size.setter
	def size(self, value):
		self.rect.size = value

	@pos.setter
	def pos(self, value):
		self.rect.pos = value		
	
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
		self.color = self.init_color
		self.size = self.init_size
		self.pos = self.init_pos
		self.texture = None
		
	def update(self,dt):
		super().update(dt)
		
	#<----Window Functions: re_size, show, hide, remove
	def re_size(self):
		pass
		
	def show(self):
		super().show()
		
		if not self.in_cnvs:
			self.window.canvas.add(self.colour)
			self.window.canvas.add(self.rect)
			self.in_cnvs = True
			
	def hide(self):
		super().hide()
		
		if self.in_cnvs:
			self.window.canvas.remove(self.colour)
			self.window.canvas.remove(self.rect)
			self.in_cnvs = False
			
	def remove(self):
		super().remove()
		
		self.hide()
		
		del(self.colour)
		del(self.rect)
		

		
	
		
		
		












