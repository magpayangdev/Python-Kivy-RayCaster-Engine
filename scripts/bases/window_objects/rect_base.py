
from scripts.bases.window_objects.window_object import WindowObject
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle


_COLOR, _SIZE, _POS, _HIDE = (1,1,1,1), (100,100), (0,0), False

	
class RectBase(WindowObject):
	""" The base class for all objects that requires a color and rectangle instruction """	
	def __init__(self, game, window, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().__init__(game=game, window=window)
		
		self.rect = None
		self.colour = None
		self.in_cnvs = False
		
		with self.window.canvas:
			self.colour = Color(rgba=color)
			self.rect = Rectangle(size=size, pos=pos, texture=None)
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
	def re_init(self, size=_SIZE, pos=_POS, color=_COLOR, hide=_HIDE, **kwargs):
		super().re_init()
		
		self.color = color
		self.size = size
		self.pos = pos

		if hide:
			if self.in_cnvs:
				self.window.canvas.remove(self.colour)
				self.window.canvas.remove(self.rect)
				self.in_cnvs = False
		else:
			if not self.in_cnvs:
				self.window.canvas.add(self.colour)
				self.window.canvas.add(self.rect)
				self.in_cnvs = True
		
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
		

		
	
		
		
		












