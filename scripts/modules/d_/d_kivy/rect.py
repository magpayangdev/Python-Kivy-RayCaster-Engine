
"""
"""

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class Rect:
	def __init__(self, game, color=(1,0,0,0), size=(100,100), pos=(0,0), hide=False):
		self.game = game
		self.window = self.game.window
		self.color = color
		self.size = size
		self.pos = pos

		with self.window.canvas:
			self.colour = Color(rgba=self.color)
			self.rect = Rectangle(size=self.size, pos=self.pos)
			self.in_cnvs =True

		if hide:
			self.hide()
		
	def re_init(self):
		self.rect.size = self.size
		self.rect.pos = self.pos
		
	def update(self, dt):
		pass
		
	def show(self):
		if not self.in_cnvs:
			self.window.canvas.add(self.colour)
			self.window.canvas.add(self.rect)
			self.in_cnvs = True
			
	def hide(self):
		if self.in_cnvs:
			self.window.canvas.remove(self.colour)
			self.window.canvas.remove(self.rect)
			self.in_cnvs = False
			
	def remove(self):
		if self.in_cnvs:
			self.hide()

	
class FullScrRect(Rect):
	def __init__(self, game, color, hide):
		super().__init__(game, color, hide=hide)
		self.size = self.window.size
		self.pos = self.window.pos
		
		self.re_init()
		

from scripts.modules.textures import *
class TexturedRect(Rect):
	def __init__(self, game, image_name, texture_category, size = (100,100), pos = (0,0), hide = False):
		super().__init__(game, color=(1,1,1,1), size=size, pos=pos, hide=hide)
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
			
		elif texture_category == 'floor':
			self.texture = flr_texture()
			
		else:
			raise Exception('Invalid image_name or texture_category')
			
		self.rect.texture = self.texture

#from scripts.game.textures import *		
class FullScrTexturedRect(TexturedRect):
	def __init__(self, game,  image_name, texture_category, hide=False):
		super().__init__(game,  image_name, texture_category, hide=hide)
		self.size = self.window.size
		self.pos = self.window.pos
		
		self.re_init()
		
class TimedRect(Rect):
	def __init__(self, game, flip_time, size=(100,100), pos=(0,0), hide=False):
		super().__init__(game, color=(1,1,1,1), size=size, pos=pos, hide=hide)
		self.accum_time = 0
		self.flip_time = flip_time
		
	def update(self, dt):
		self.accum_time += dt
		self.fbf_update(dt)
		
		if self.accum_time > self.flip_time:
			self.accum_time = 0
			self.timed_update()
			
	def fbf_update(self, dt):
		pass
		
	def timed_update(self):
		pass

#from scripts.game.textures import *		
class d_SeqTexRect(TimedRect):
	''' Sequenced Textured Rectangle '''
	def __init__(self, game, seq_name, initial_mode, flip_time, animate, size=(100,100), pos=(0,0), hide = False):
		super().__init__(game, flip_time=flip_time, size=size, pos=pos, hide=hide)
		self.sprt_id = seq_name
		self.mode = initial_mode
		self.animate = animate
		self.do_once = True
		self.loop_flag = False
		
		self.reload_texture()
	
	def fbf_update(self, dt):
		super().fbf_update(dt)
		pass
	
	def timed_update(self):
		super().timed_update()
		
		if not self.animate:
			return 
			
		try:
			if self.do_once:
				self.do_once_func()	
				
			self.try_func()
			
		except StopIteration:
			self.stop_iteration_func()
	
	#<---- Timed Update		
	def do_once_func(self):
		self.do_once = False
		
	def try_func(self):
		self.rect.texture = next(self.seq_texture)
		
	def stop_iteration_func(self):
		self.do_once = True
		self.reload_texture()
		self.animate = self.loop_flag
		
	#<---- Start Resume Stop	
	def start(self):
		self.reload_texture()
		self.resume()
		
	def resume(self):
		self.animate = True
		self.loop_flag = False
		
	def loop(self):
		self.animate = True
		self.loop_flag = True
		
	def stop(self):
		self.loop_flag = False
		
	#<---- Textures Func
	def reload_texture(self):
		self.seq_texture = (image for image in get_image_sequence(self.sprt_id, self.mode))
		self.rect.texture = next(self.seq_texture)
		
	def change_mode(self, new_mode):
		self.mode = new_mode
		self.reload_texture()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		