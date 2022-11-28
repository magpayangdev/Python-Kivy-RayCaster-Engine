
from scripts.game.textures import *
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class RectArray:
	def __init__(self, game, color=(1,1,1,1), num_rects=2, size=(100,100), pos=(0,0), offset=0, hide=False):
		self.game=game
		self.window=self.game.window
		self.in_cnvs = False	

		self.num_rects = num_rects
		self.size = size
		self.pos = pos
		self.color = color
		self.offset = offset
		
		with self.window.canvas:
			self.rects = tuple((Color(rgba=self.color),Rectangle(size=self.size)) for _ in range(self.num_rects))
			self.in_cnvs = True
			
		if hide:
			self.hide()
			
	def re_init(self):
		fpos = lambda idx: ((self.pos[0] + self.offset + self.size[0]) * idx, self.pos[1])
		for idx, entry in enumerate(self.rects):
			entry[1].size = self.size
			entry[1].pos = fpos(idx)

	def update(self, dt):
		pass
		
	def flip(self):
		pass

	def show(self):
		if not self.in_cnvs:
			self.in_cnvs = True
			f = lambda x: (self.window.canvas.add(x[0]), self.window.canvas.add(x[1]))
			[f(entry) for entry in self.rects]
		
	def hide(self):
		if self.in_cnvs:
			self.in_cnvs = False
			f = lambda x: (self.window.canvas.remove(x[0]), self.window.canvas.remove(x[1]))
			[f(entry) for entry in self.rects]
		
	def remove(self):
		if self.in_cnvs:
			self.hide()
		

from scripts.game.textures import *			
class TexturedRectArray(RectArray):
	def __init__(self, game, image_name, texture_category, num_digits=3, size=(100,100), pos=(0,0), offset=1, hide=False):
		super().__init__(game, color=(1,1,1,1), num_rects=num_digits, size=size, pos=pos, offset=offset, hide=hide)
		
		if texture_category == 'controller':
			self.texture = get_controller_texture(image_name)
			
		elif texture_category == 'digits':
			self.texture = get_digit_texture(image_name)
			
		elif texture_category == 'game':
			self.texture = get_game_texture(image_name)
						
		elif texture_category == 'map':
			self.texture = get_map_texture(image_name)
			
		elif texture_category == 'menu':
			self.texture = get_menu_texture(image_name)
			
		elif texture_category == 'sky':
			self.texture = get_sky_texture(image_name)
			
		elif texture_category == 'wall':
			self.texture = get_wall_texture(image_name)
			
		else:
			raise Exception('Invalid image_name or texture_category')
			
		for idx, entry in enumerate(self.digits):
			entry[1].texture = self.texture

class DigitalRegister(RectArray):
	def __init__(self, game, num_digits=3, size=(100,100), pos=(0,0), offset=1, hide=False):
		super().__init__(game, color=(1,1,1,1), num_rects=num_digits, size=size, pos=pos, offset=offset, hide=hide)
		
	def show(self):
		super().show()
		self.flip()

	def flip(self, value=100):
		a = int(value)
		
		for idx, entry in enumerate(self.rects):
			num = a // (100 // (10 ** idx))
			entry[1].texture = get_digit_texture(str(num))
			a = a % (100 // (10 ** idx))
			
			

			
			
			
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
			
			
			
			
			
			