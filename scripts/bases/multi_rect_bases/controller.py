
from scripts.modules.textures import *
from settings import *
import math

from scripts.bases.multi_rect_bases.nested_rect import NestedRect

class Controller(NestedRect):
	def __init__(self, game, window=None, orientation='right', img_name_1='dotted_circle.png', img_name_2='circle.png', size=controller_size(), offset=controller_size()[0]/3, pressed_color=(1,1,0,1), normal_color=(1,1,1,1), hide=True):

		super().__init__(game=game, window=window, num_rects=2, size=size, pos=(0,0), offset=offset, hide=hide)

		self.img_name_1 = img_name_1
		self.img_name_2 = img_name_2
		self.orientation = orientation

		self.rects[0].texture = get_controller_texture(self.img_name_1)
		self.rects[1].texture = get_controller_texture(self.img_name_2)
		
		if self.orientation == 'left':
			self.center = controller_center_left()
			
		elif self.orientation == 'right':
			self.center = controller_center_right()
			
		else:
			raise Exception('Invalid orientation: {}'.format(self.orientation))
			
		f = lambda idx: self.center[idx] - self.size[idx] / 2
		self.pos = tuple(f(idx) for idx, pos in enumerate(self.pos))		
		
		self.re_size()		
		
		self.accum_time = 9999
		self.start_count = False
		self.normal_color = normal_color
		self.pressed_color = pressed_color
		self.stick_size = self.rects[1].rect.size
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()	
		
		self.rects[0].texture = get_controller_texture(self.img_name_1)
		self.rects[1].texture = get_controller_texture(self.img_name_2)
		
		if self.orientation == 'left':
			self.center = controller_center_left()
			
		elif self.orientation == 'right':
			self.center = controller_center_right()
			
		else:
			raise Exception('Invalid orientation: {}'.format(self.orientation))
			
		f = lambda idx: self.center[idx] - self.size[idx] / 2
		self.pos = tuple(f(idx) for idx, pos in enumerate(self.pos))		
		
		self.re_size()		
		
		self.accum_time = 9999
		self.start_count = False
		self.stick_size = self.rects[1].rect.size

	def update(self,dt):		
		if not self.start_count:
			return
		
		self.accum_time += dt
		
		if self.accum_time > 1:
			self.accum_time = 9999
			self.start_count = False
			
	def flip(self):
		if self.accum_time < 1:
			self.flip_func()
			
	def flip_func(self):
		self.stop_counting()
			
	def start_counting(self):
		self.start_count = True
		self.accum_time = 0
		self.rects[1].color = self.pressed_color
		
	def stop_counting(self):
		self.start_count = False
		self.accum_time = 9999
		self.rects[1].color = self.normal_color
				
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()	
		
	def reset_stick(self):
		self.move_stick(*self.center)
		
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


