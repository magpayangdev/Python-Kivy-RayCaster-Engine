
from scripts.bases.timed_updates.timed_update import TimedUpdate
from scripts.bases.window_objects.rect_base import RectBase

_FLIP_TIME, _START_ITER = 1, False
_COLOR, _SIZE, _POS, _HIDE = (1,1,1,1), (100,100), (0,0), False


class TimedRect(TimedUpdate):
	def __init__(self, game, window, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().__init__(game, flip_time=flip_time, start_iter=start_iter)
		
		self.rect_comp = RectBase(game=game, window=window, color=color, size=size, pos=pos, hide=hide)

	#<----Getters		
	@property
	def window(self):
		return self.rect_comp.window
		
	@property
	def rect(self):
		return self.rect_comp.rect
		
	@property
	def colour(self):
		return self.rect_comp.colour
		
	@property
	def rect_size(self):
		return self.rect_comp.rect.size
		
	@property
	def rect_pos(self):
		return self.rect_comp.rect.pos

	#<----Setters		
	@rect_size.setter
	def rect_size(self, value):
		self.rect_comp.size = value
		self.rect_comp.rect.size = self.rect_comp.size
		
	@rect_pos.setter
	def rect_pos(self, value):
		self.rect_comp.pos = value
		self.rect_comp.rect.pos = self.rect_comp.pos
		
	@colour.setter
	def rect_colour(self, value):
		self.rect_comp.color = value
		self.rect_comp.colour.rgba = self.rect_comp.color		

	#<----Base Functions: re_init, update
	def re_init(self, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().re_init(flip_time=flip_time, start_iter=start_iter)
		self.rect_comp.re_init(color=color, size=size, pos=pos, hide=hide)
		
	def update(self, dt):
		super().update(dt)
		self.rect_comp.update(dt)

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		super().fbf_update(dt)
				
	def timed_update(self):
		super().timed_update()
				
	#<----Timed Update Functions: do_once_func, try_func, stop_iteration_func	
	def do_once_func(self):
		super().do_once_func()
					
	def try_func(self):
		super().try_func()
				
	def stop_iteration_func(self):
		super().stop_iteration_func()
				
	#<----Loop Controls: start, resume, loop, stop	
	def start(self):
		super().start()
				
	def resume(self):		
		super().resume()
				
	def loop(self):
		super().loop()
				
	def stop(self):
		super().stop()

	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		self.rect_comp.re_size()

	def show(self):
		self.rect_comp.show()
					
	def hide(self):
		self.rect_comp.hide()
					
	def remove(self):
		self.rect_comp.remove()		
























