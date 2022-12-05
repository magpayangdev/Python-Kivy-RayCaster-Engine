
from scripts.bases.timed_updates.timed_update import TimedUpdate
from scripts.bases.window_objects.sequence_textured_rect import SequenceTexturedRect

_FLIP_TIME, _START_ITER = 1, True
_IMG_SEQ_ID, _INITIAL_MODE = 'soldier', 'idle'
_COLOR, _SIZE, _POS, _HIDE = (1,1,1,1), (100,100), (0,0), False


class TimedImageSequence(TimedUpdate):
	""" A TimedUpdate that has a rectangle
			Adds the Rectangle and Textures functions """
	def __init__(self, game, window, img_seq_id=_IMG_SEQ_ID, initial_mode=_INITIAL_MODE, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().__init__(game=game, flip_time=flip_time, start_iter=start_iter)
		
		self.sequence_textured_rect = SequenceTexturedRect(game=game, window=window, img_seq_id=img_seq_id, initial_mode=initial_mode, color=color, size=size, pos=pos, hide=hide)

	#<----Sequence Textured Rect Functions
	#<----Getters
	@property
	def img_seq_id(self):
		return self.sequence_textured_rect.img_seq_id
	
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
	def re_init(self, img_seq_id=_IMG_SEQ_ID, initial_mode=_INITIAL_MODE, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER):
		super().re_init(flip_time=flip_time, start_iter=start_iter)
		
		self.sequence_textured_rect.re_init(img_seq_id=img_seq_id, initial_mode=initial_mode, color=color, size=size, pos=pos, hide=hide)
		
	def update(self, dt):
		super().update(dt)
		self.sequence_textured_rect.update(dt)

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
		
		self.sequence_textured_rect.rect.texture = next(self.sequence_textured_rect.seq_texture)		
		
	def stop_iteration_func(self):
		super().stop_iteration_func()
		
		self.reload_texture()
		
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
		pass
		
	def show(self):
		self.sequence_textured_rect.show()
			
	def hide(self):
		self.sequence_textured_rect.hide()
					
	def remove(self):
		self.sequence_textured_rect.remove()

	#<----Textures Functions: reload, change mode
	def reload_texture(self):
		self.sequence_textured_rect.reload_texture()
		
	#def change_mode(self, new_mode):
		#self.sequence_textured_rect.change_mode(new_mode)	


		

		

		





















