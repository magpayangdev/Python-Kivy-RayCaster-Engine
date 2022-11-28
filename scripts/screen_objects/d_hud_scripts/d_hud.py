#from scripts.bases.quadrant_bases.hud_base import HudBase

from scripts.bases.touch_objects.hud_base import HudBase

class Hud(HudBase):
	def __init__(self, game, flip_time=1, start_iter=False, hide=False):
		super().__init__(game=game, flip_time=flip_time, start_iter=start_iter, hide=hide)
		
	#<---- Window Func
	def show(self):
		super().show()
		
	def hide(self):
		super().hide()
		
	def remove(self):
		super().remove()
		
	#<----Base Functions: re_init, update
	def re_init(self):
		super().re_init()
		
	def update(self, dt):
		super().update(dt)

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

	#<---- Touch Down
	def on_touch_down(self, touch):
		super().on_touch_down(touch)
	
	#<---- Touch Move	
	def on_touch_move(self, touch):
		super().on_touch_move(touch)
		
	#<---- Touch Up
	def on_touch_up(self, touch):
		super().on_touch_up(touch)
			
	#<---- Touch Down
	def touch_down_q1(self, touch):
		super().touch_down_q1(touch)

	def touch_down_q2(self, touch):
		super().touch_down_q2(touch)
		
	def touch_down_q3(self, touch):
		super().touch_down_q3(touch)
		
	def touch_down_q4(self, touch):
		super().touch_down_q4
		
	#<---- Touch Move
	def touch_move_q1(self, touch):
		super().touch_move_q1(touch)
		
	def touch_move_q2(self, touch):
		super().touch_move_q2(touch)
		
	def touch_move_q3(self, touch):
		super().touch_move_q3(touch)
		
	def touch_move_q4(self, touch):
		super().touch_move_q4(touch)
		
	#<---- Touch Up
	def touch_up_q1(self, touch):
		super().touch_up_q1(touch)
		
	def touch_up_q2(self, touch):
		super().touch_up_q2(touch)
		
	def touch_up_q3(self, touch):
		super().touch_up_q3(touch)
		
	def touch_up_q4(self, touch):
		super().touch_up_q4(touch)
		
		