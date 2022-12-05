
from scripts.bases.timed_updates.timed_update import TimedUpdate
from scripts.bases.touch_objects.hud_base import HudBase


_HIDE, _FLIP_TIME, _START_ITER = False, 1, True

class TimedQuadrant(TimedUpdate):
	def __init__(self, game, window=None, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().__init__(game=game, flip_time=flip_time, start_iter=start_iter)
		
		self.quadrant = HudBase(game=game, window=window)
		
	#<----Properties
	@property
	def player_health(self):
		return self.quadrant.player_health
	
	@property
	def text(self):
		return self.quadrant.text
		
	@text.setter
	def text(self, value):
		self.quadrant.text = value
		
	@property
	def player_sprite(self):
		return self.quadrant.player_sprite
		
	@property
	def hit_rect(self):
		return self.quadrant.hit_rect
		
	@property
	def left_controller(self):
		return self.quadrant.left_controller
		
	@property
	def right_controller(self):
		return self.quadrant.right_controller
	
	#<----Hud Base Functions
	def reset_hud(self):
		self.quadrant.reset_hud()
			
	def game_over(self):
		self.quadrant.game_over()
		
	def victory(self):
		self.quadrant.victory()

	def player_is_hit(self):			
		self.quadrant.player_is_hit()
		
	#<----Base Functions: re_init, update
	def re_init(self, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().re_init(flip_time=flip_time, start_iter=start_iter)
		self.quadrant.re_init()
		
	def update(self, dt):
		super().update(dt)
		self.quadrant.update(dt)

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		super().fbf_update(dt)

		self.player_sprite.update(dt)
		self.left_controller.update(dt)
		self.right_controller.update(dt)		
		
	def timed_update(self):
		super().timed_update()
		
		if self.quadrant.reset_hit_rect:
			self.quadrant.reset_hit_rect = False
			self.quadrant.hit_rect.color = 0,0,0,0
			
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
		
	#<----Window Functs
	def re_size(self):
		pass
		
	def show(self):
		self.quadrant.show()
		
	def hide(self):
		self.quadrant.hide()
		
	def remove(self):
		self.quadrant.remove()

	#<---- Touch Down
	def on_touch_down(self, touch):
		self.quadrant.on_touch_down(touch)
	
	#<---- Touch Move	
	def on_touch_move(self, touch):
		self.quadrant.on_touch_move(touch)
		
	#<---- Touch Up
	def on_touch_up(self, touch):
		self.quadrant.on_touch_up(touch)
			
	#<---- Touch Down
	def touch_down_q1(self, touch):
		self.quadrant.touch_down_q1(touch)

	def touch_down_q2(self, touch):
		self.quadrant.touch_down_q2(touch)
		
	def touch_down_q3(self, touch):
		self.quadrant.touch_down_q3(touch)
		
	def touch_down_q4(self, touch):
		self.quadrant.touch_down_q4(touch)
		
	#<---- Touch Move
	def touch_move_q1(self, touch):
		self.quadrant.touch_move_q1(touch)
		
	def touch_move_q2(self, touch):
		self.quadrant.touch_move_q2(touch)
		
	def touch_move_q3(self, touch):
		self.quadrant.touch_move_q3(touch)
		
	def touch_move_q4(self, touch):
		self.quadrant.touch_move_q4(touch)
		
	#<---- Touch Up
	def touch_up_q1(self, touch):
		self.quadrant.touch_up_q1(touch)
		
	def touch_up_q2(self, touch):
		self.quadrant.touch_up_q2(touch)
		
	def touch_up_q3(self, touch):
		self.quadrant.touch_up_q3(touch)
		
	def touch_up_q4(self, touch):
		self.quadrant.touch_up_q4(touch)





