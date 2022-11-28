
import math
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class NestedRect:
	def __init__(self, game, color_1=(0.5,0.5,0.5,1), size_1=(250.0,250.0), color_2=(0.1,0.1,0.1,1), size_2=(100.0,100.0), pos=(0,0), hide=False):
		self.game = game
		self.window = self.game.window
		self.color_1 = color_1
		self.size_1 = size_1
		self.color_2 = color_2
		self.size_2 = size_2
		self.pos_1 = pos
		x = self.pos_1[0]+ (self.size_1[0]/2) - self.size_2[0]/2
		y = self.pos_1[1]+ (self.size_1[1]/2) - self.size_2[1]/2
		self.pos_2 = x,y
		
		self.is_active=False
	
		with self.window.canvas:
			self.colour_1 = Color(rgba=self.color_1)
			self.rect_1 = Rectangle(size=self.size_1,pos=self.pos_1)
		
			self.colour_2 = Color(rgba=self.color_2)
			self.rect_2 = Rectangle(size=self.size_2,pos=self.pos_2)
			
			self.in_cnvs=True

		if hide:
			self.hide()
		
	def re_init(self):
		self.rect_1.size = self.size_1
		self.rect_1.pos = self.pos_1	
		self.rect_2.size = self.size_2
		x = self.pos_1[0] + (self.size_1[0]/2) - self.size_2[0]/2
		y = self.pos_1[1] + (self.size_1[1]/2) - self.size_2[1]/2	
		self.rect_2.pos = x,y
				
	def update(self, dt):
		pass
		
	def show(self):
		if not self.in_cnvs:
			self.window.canvas.add(self.colour_1)
			self.window.canvas.add(self.rect_1)
			self.window.canvas.add(self.colour_2)
			self.window.canvas.add(self.rect_2)
			self.in_cnvs=True
		
	def hide(self):
		if self.in_cnvs:
			self.window.canvas.remove(self.colour_1)
			self.window.canvas.remove(self.rect_1)
			
			self.window.canvas.remove(self.colour_2)
			self.window.canvas.remove(self.rect_2)
			self.in_cnvs=False
		
	def remove(self):
		if self.in_cnvs:
			self.hide()
			
	def move_rect_2(self, Px, Py):		
		self.rect_2.pos = Px - self.size_2[0] / 2, Py - self.size_2[1] / 2 
			
	def reset_rect_2(self):
		x = self.pos_1[0] + (self.size_1[0]/2) - self.size_2[0]/2
		y = self.pos_1[1] + (self.size_1[1]/2) - self.size_2[1]/2	
		self.rect_2.pos = x,y


from scripts.game.textures import *
class TexturedNestedRect(NestedRect):
	def __init__(self, game, img_name_1, texture_category_1, img_name_2, texture_category_2, size_1=(250.0,250.0), size_2=(100.0,100.0), pos=(0,0), hide=False):
		super().__init__(game,color_1=(1,1,1,1),color_2=(1,1,1,1),size_1=size_1,size_2=size_2,pos=pos,hide=hide)

		self.rect_1.texture = self.get_texture(img_name_1, texture_category_1)
		self.rect_2.texture = self.get_texture(img_name_2, texture_category_2)

	def get_texture(self, image_name, texture_category):
		if texture_category == 'controller':
			return get_controller_texture(image_name)
			
		elif texture_category == 'digits':
			return get_digit_texture(image_name)
			
		elif texture_category == 'game':
			return get_game_texture(image_name)
						
		elif texture_category == 'map':
			return get_map_texture(image_name)
			
		elif texture_category == 'menu':
			return get_menu_texture(image_name)
			
		elif texture_category == 'sky':
			return get_sky_texture(image_name)
			
		elif texture_category == 'wall':
			return get_wall_texture(image_name)
			
		else:
			raise Exception('Invalid image_name or texture_category')
	
			

		
		
		
	














	
		