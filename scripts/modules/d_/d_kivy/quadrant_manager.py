
class QManager:
	def __init__(self, game):
		self.game = game
		self.window = self.game.window
		self.accum_time = 0
		self.in_cnvs = False
		self.flip_time = 1
		
	def re_init(self):
		pass
		
	def update(self, dt):
		self.accum_time += dt
		self.fbf_update(dt)
		
		if self.accum_time > self.flip_time:
			self.accum_time = 0
			self.timed_update()
			
	def fbf_update(self, dt):
		pass
		
	def timed_update(self):
		pass
		
	def show(self):
		self.in_cnvs = True
		
	def hide(self):
		self.in_cnvs = False
		
	def remove(self):
		self.in_cnvs = False
		












































