
from scripts.bases.base import Base

_FLIP_TIME, _START_ITER = 1, False


class TimedUpdate(Base):
	""" Counts elapsed time and resets counter after a specified duration """
	def __init__(self, game, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().__init__(game=game)
		self.flip_time = flip_time
		self.start_iter = start_iter

		self.accum_time = 0
		self.do_once = True
		self.loop_flag = False

	#<----Base Functions: re_init, update
	def re_init(self, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().re_init()
		
		self.flip_time = flip_time
		self.start_iter = start_iter
		
		self.accum_time = 0
		self.do_once = True
		self.loop_flag = False
		
	def update(self, dt):
		super().update(dt)
		
		if not self.start_iter:
			return
		
		self.accum_time += dt
		self.fbf_update(dt)
		
		if self.accum_time > self.flip_time:
			self.accum_time = 0
			self.timed_update()

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		pass
		
	def timed_update(self):
		if self.do_once:
			self.do_once = False
			self.do_once_func()

		try:
			self.try_func()
			
		except StopIteration:
			self.stop_iteration_func()
		
	#<----Timed Update Functions: do_once_func, try_func, stop_iteration_func	
	def do_once_func(self):
		pass
			
	def try_func(self):
		pass
		
	def stop_iteration_func(self):
		self.do_once = True
		self.start_iter = self.loop_flag
		
	#<----Loop Controls: start, resume, loop, stop	
	def start(self):
		self.resume()
		
	def resume(self):		
		self.start_iter = True
		self.loop_flag = False
		
	def loop(self):
		self.start_iter = True
		self.loop_flag = True
		
	def stop(self):
		self.loop_flag = False
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		