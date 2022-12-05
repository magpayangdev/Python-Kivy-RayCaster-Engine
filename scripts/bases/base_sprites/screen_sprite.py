
from scripts.bases.timed_updates.timed_image_sequence import TimedImageSequence

_FLIP_TIME, _START_ITER = 1, False
_SCREEN_SIZE, _SCREEN_POS, _HIDE = (100,100), (0,0), False
_SPRITE_ID, _INITIAL_MODE, _COLOR = 'shot_gun', 'idle', (1,1,1,1)


class ScreenSprite(TimedImageSequence):
	def __init__(self, game, window, sprite_id=_SPRITE_ID, initial_mode=_INITIAL_MODE,
					color=_COLOR, screen_size=_SCREEN_SIZE, screen_pos=_SCREEN_POS,
						hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().__init__(game=game, window=window, img_seq_id=sprite_id, initial_mode=initial_mode,
							color=color, size=screen_size, pos=screen_pos, hide=hide, flip_time=flip_time,
								start_iter=start_iter)

	#<----Sequence Textured Rect Functions
	#<----Getters
	@property
	def window(self):
		return self.sequence_textured_rect.window

	@property
	def rect(self):
		return self.sequence_textured_rect.rect
		
	@property
	def size(self):
		return self.sequence_textured_rect.rect.size
		
	@property
	def pos(self):
		return self.sequence_textured_rect.rect.pos
				
	@property
	def mode(self):
		return self.sequence_textured_rect.mode
	
	#<----Setters
	@size.setter
	def size(self, value):
		self.sequence_textured_rect.rect.size = value
		
	@pos.setter
	def pos(self, value):
		self.sequence_textured_rect.rect.pos = value

	@mode.setter
	def mode(self, value):
		self.sequence_textured_rect.change_mode(value)

	#<----Base Functions: re_init, update
	def re_init(self, sprite_id=_SPRITE_ID, initial_mode=_INITIAL_MODE, color=_COLOR,
					screen_size=_SCREEN_SIZE, screen_pos=_SCREEN_POS, hide=_HIDE,
						flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().re_init(img_seq_id=sprite_id, initial_mode=initial_mode, color=color,
							size=screen_size, pos=screen_pos, hide=hide, flip_time=flip_time,
								start_iter=start_iter)
		
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
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
					
	def remove(self):
		super().remove()

	#<----Textures Functions: reload, change mode
	def reload_texture(self):
		super().reload_texture()
		
	def change_mode(self, new_mode):
		super().change_mode(new_mode)