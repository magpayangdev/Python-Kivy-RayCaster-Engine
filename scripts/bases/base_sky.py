
from scripts.bases.timed_updates.timed_texture import TimedTexture
from scripts.modules.textures import *
from settings import *
import math


_IMAGE_NAME, _IMAGE_CATEGORY, _HIDE = 'dark_night_sky.png', 'sky', False


class BaseSky(TimedTexture):
	def __init__(self, game, image_name=_IMAGE_NAME, hide=_HIDE):
		super().__init__(game, window=None, image_name=image_name, image_category=_IMAGE_CATEGORY, hide=hide)
		
		self.flip_time = self.rect.texture.width

		self.rect_size = self.game.window.width, self.game.window.height/2
		self.rect_pos = self.game.window.pos[0], self.game.window.height/2

	#<----Base Functions: re_init, update
	def re_init(self, image_name=_IMAGE_NAME, hide=_HIDE):
		super().re_init(image_name=image_name, image_category=_IMAGE_CATEGORY, hide=hide)

		self.flip_time = self.rect.texture.width

		self.rect_size = self.game.window.width, self.game.window.height/2
		self.rect_pos = self.game.window.pos[0], self.game.window.height/2

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		super().fbf_update(dt)
		
		if self.game.player:
			yaw = self.game.player.yaw
		else:
			yaw = self.accum_time
		
		uv_pos = (0,0)
		if yaw == 0:
			uv_pos = ((self.rect_texture.uvpos[0] + 1 * dt * 0.005) % self.rect_texture.width, 
						self.rect_texture.uvpos[1])

		else:
			uv_pos = ((self.rect_texture.uvpos[0] + 0.001 * dt * yaw) % self.rect_texture.width, 
						self.rect_texture.uvpos[1])

		self.rect_texture.uvpos = uv_pos
		self.rect_texture = self.rect_texture
	