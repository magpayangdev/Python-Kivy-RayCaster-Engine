
from scripts.modules.textures import *
from settings import *
import math

from scripts.bases.multi_rect_bases.nested_rect import NestedRect

class Controller(NestedRect):
	def __init__(self, game, window=None, orientation='right', img_name_1='dotted_circle.png', img_name_2='dotted_circle.png', size=controller_size(), offset=controller_size()[0]/3, hide=True):

		super().__init__(game=game, window=window, num_rects=2, size=size, pos=(0,0), offset=offset, hide=hide)

		self.init_img_name_1 = img_name_1
		self.init_img_name_2 = img_name_2
		self.init_orientation = orientation

		self.rects[0].rect.texture = get_controller_texture(self.init_img_name_1)
		self.rects[1].rect.texture = get_controller_texture(self.init_img_name_2)
		
		if self.init_orientation == 'left':
			self.center = controller_center_left()
			
		elif self.init_orientation == 'right':
			self.center = controller_center_right()
			
		else:
			raise Exception('Invalid orientation: {}'.format(self.init_orientation))
		
		self.stick_size = self.rects[1].rect.size
		
		self.accum_time = 9999
		self.start_count = False
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()	
		
		self.rects[0].rect.texture = get_controller_texture(self.init_img_name_1)
		self.rects[1].rect.texture = get_controller_texture(self.init_img_name_2)
		
		if self.init_orientation == 'left':
			self.center = controller_center_left()
			
		elif self.init_orientation == 'right':
			self.center = controller_center_right()
			
		else:
			raise Exception('Invalid orientation: {}'.format(self.init_orientation))
		
		self.stick_size = self.rects[1].rect.size
		
		self.accum_time = 9999
		self.start_count = False
		
	def update(self,dt):
		#super().update(dt)
		
		if not self.start_count:
			return
		
		self.accum_time += dt
		
		if self.accum_time > 1:
			self.accum_time = 9999
			self.start_count = False
			
	def start_counting(self):
		self.start_count = True
		self.accum_time = 0
		
	def stop_counting(self):
		self.start_count = False
		self.accum_time = 9999
		
	def flip(self):
		pass
				
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()	
		
	def move_stick(self, Px, Py):
		dist = math.dist((Px,Py), self.center)
		
		if dist > self.size[0] / 2:
			Px = (self.size[0]/2) * (Px - self.center[0]) / dist + self.center[0]
			Py = (self.size[1]/2) * (Py - self.center[1]) / dist + self.center[1]
		
		self.rects[1].rect.pos = Px - self.stick_size[0] / 2, Py - self.stick_size[1] / 2

class LeftController(Controller):
	def __init__(self, game):
		super().__init__(game, orientation='left')
		
class RightController(Controller):
	def __init__(self, game):
		super().__init__(game, orientation='right')


