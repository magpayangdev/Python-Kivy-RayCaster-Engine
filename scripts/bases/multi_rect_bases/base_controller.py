
import math
from settings import *
from scripts.modules.textures import *
from scripts.bases.multi_rect_bases.nested_rect import NestedRect

_NUM_RECTS, _POS = 2, (0,0)
_PRESSED_COLOR, _NORMAL_COLOR, _HIDE = (1,1,0,1), (1,1,1,1), True
_SIZE, _POS, _OFFSET = controller_size(), (0,0), controller_size()[0]/3
_ORIENTATION, _IMG_NAME_1, _IMG_NAME_2 = 'right', 'dotted_circle.png', 'circle.png'


class BaseController(NestedRect):
	def __init__(self, game, window=None, orientation=_ORIENTATION, img_name_1=_IMG_NAME_1, img_name_2=_IMG_NAME_2, size=_SIZE, offset=_OFFSET, pressed_color=_PRESSED_COLOR, normal_color=_NORMAL_COLOR, hide=_HIDE):
		
		f = lambda idx, size: controller_center_left()[idx] - size[idx] / 2
		g = lambda idx, size: controller_center_right()[idx] - size[idx] / 2
	
		positioning_lambda = lambda window, size, pos, offset: tuple(f(i, size) for i in range(2)) if orientation=='left' else tuple(g(i, size) for i in range(2))	

		super().__init__(game=game, window=window, num_rects=_NUM_RECTS, size=size, pos=(0,0),  offset=offset, positioning_lambda=positioning_lambda, hide=hide)
		
		self.accum_time = 9999
		self.start_count = False
		self.normal_color = normal_color
		self.pressed_color = pressed_color
		self.stick_size = self.rects[1].rect.size
		self.center = self.controller_center(orientation)
		
		self.rects[0].texture = get_texture(img_name_1, 'controller')
		self.rects[1].texture = get_texture(img_name_2, 'controller')
		
	#<----Base Functions: re_init, update			
	def re_init(self, orientation=_ORIENTATION, img_name_1=_IMG_NAME_1, img_name_2=_IMG_NAME_2, size=_SIZE, offset=_OFFSET, pressed_color=_PRESSED_COLOR, normal_color=_NORMAL_COLOR, hide=_HIDE):
		
		f = lambda idx, size: controller_center_left()[idx] - size[idx] / 2
		g = lambda idx, size: controller_center_right()[idx] - size[idx] / 2
	
		positioning_lambda = lambda window, size, pos, offset: tuple(f(i, size) for i in range(2)) if orientation=='left' else tuple(g(i, size) for i in range(2))

		super().re_init(size=size, pos=(0,0), offset=offset, positioning_lambda=positioning_lambda, hide=hide)
		
		self.accum_time = 9999
		self.start_count = False
		self.normal_color = normal_color
		self.pressed_color = pressed_color
		self.stick_size = self.rects[1].rect.size
		self.center = self.controller_center(orientation)
		
		self.rects[0].texture = get_texture(img_name_1, 'controller')
		self.rects[1].texture = get_texture(img_name_2, 'controller')
		
	#<----Controller Funcs
	def controller_pos(self, size, init_pos, orientation):
		center = self.controller_center(orientation)
			
		f = lambda idx: center[idx] - size[idx] / 2
		
		return tuple(f(idx) for idx, pos in enumerate(init_pos))
		
	def controller_center(self, orientation):
		center = 0,0
		
		if orientation == 'left':
			center = controller_center_left()
		elif orientation == 'right':
			center = controller_center_right()
		else:
			raise Exception('Invalid orientation: {}'.format(orientation))	
			
		return center	

	def update(self,dt):		
		if not self.start_count:
			return
		
		self.accum_time += dt
		if self.accum_time > 1:
			self.accum_time = 9999
			self.start_count = False
			self.rects[1].color = self.normal_color
			
	def flip(self):
		if self.accum_time < 1:
			self.flip_func()
			
	def flip_func(self):
		self.stop_counting()
			
	def start_counting(self):
		if self.game.loop_num == 1:
			self.start_count = True
			self.accum_time = 0
			self.rects[1].color = self.pressed_color
		
	def stop_counting(self):
		self.start_count = False
		self.accum_time = 9999
		self.rects[1].color = self.normal_color
		
	def reset_stick(self):
		self.move_stick(*self.center)
		
	def move_stick(self, Px, Py):
		dist = math.dist((Px,Py), self.center)
		
		if dist > self.size[0] / 2:
			Px = (self.size[0]/2) * (Px - self.center[0]) / dist + self.center[0]
			Py = (self.size[1]/2) * (Py - self.center[1]) / dist + self.center[1]
		
		self.rects[1].rect.pos = Px - self.stick_size[0] / 2, Py - self.stick_size[1] / 2
				
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()	
		

