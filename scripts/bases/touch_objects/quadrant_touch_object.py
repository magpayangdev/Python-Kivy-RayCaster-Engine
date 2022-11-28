
from scripts.bases.touch_objects.touch_object import TouchObject


class QuadrantTouchObject(TouchObject):
	def __init__(self, game, window):
		super().__init__(game=game)
		
		self.window=None
		if window:
			self.window = window
		else:
			self.window = game.window

	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)

	#<----TouchFunctions: on_touch_down, on_touch_move, on_touch_up
	def on_touch_down(self, touch):
		super().on_touch_down(touch)
		
		if   touch.x<=self.window.center_x and touch.y<=self.window.center_y: 		
			self.touch_down_q1(touch)
									
		elif touch.x <= self.window.center_x and touch.y > self.window.center_y:
			self.touch_down_q2(touch)
			
		elif touch.x>self.window.center_y and touch.y<=self.window.center_y: 
			self.touch_down_q3(touch)

		else: 
			self.touch_down_q4(touch)
	
	def on_touch_move(self, touch):
		super().on_touch_move(touch)
		
		if   touch.x<=self.window.center_x and touch.y<=self.window.center_y: 			
			self.touch_move_q1(touch)
									
		elif touch.x <= self.window.center_x and touch.y > self.window.center_y:
			self.touch_move_q2(touch)
			
		elif touch.x>self.window.center_y and touch.y<=self.window.center_y: 
			self.touch_move_q3(touch)

		else: 
			self.touch_move_q4(touch)
		
	def on_touch_up(self, touch):
		super().on_touch_up(touch)
		
		if touch.x <= self.window.center_x and touch.y <= self.window.center_y: 
			self.touch_up_q1(touch)
									
		elif touch.x <= self.window.center_x and touch.y > self.window.center_y: 
			self.touch_up_q2(touch)
								
		elif touch.x >  self.window.center_y and touch.y <= self.window.center_y:
			self.touch_up_q3(touch)
				
		else:						   	
			self.touch_up_q4(touch)
			
	#<---- Touch Down Funcs
	def touch_down_q1(self, touch):
		pass

	def touch_down_q2(self, touch):
		pass
		
	def touch_down_q3(self, touch):
		pass
		
	def touch_down_q4(self, touch):
		pass
		
	#<---- Touch Move Funcs
	def touch_move_q1(self, touch):
		pass
		
	def touch_move_q2(self, touch):
		pass
		
	def touch_move_q3(self, touch):
		pass
		
	def touch_move_q4(self, touch):
		pass
		
	#<---- Touch Up Funcs
	def touch_up_q1(self, touch):
		pass
		
	def touch_up_q2(self, touch):
		pass
		
	def touch_up_q3(self, touch):
		pass
		
	def touch_up_q4(self, touch):
		pass
		