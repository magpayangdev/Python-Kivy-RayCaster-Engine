
from scripts.spaces.sprites_container import SpritesContainer
import scripts.modules.loaders.sprites_loader as loader
from scripts.screen_objects.sprites import *
from settings import *
import random

_HIDE=True


class SceneSpritesContainer(SpritesContainer):
	def __init__(self, game, hide=_HIDE, **kwargs):
		super().__init__(game=game, hide=hide, **kwargs)

		self.c_t_s = None		
		self.FOV_s = []
		self.o_s = []
		self.load_list = []

		loader.init(self.game, self.load_list)	
		
	def reload_sprites(self):
		self.c_t_s = None		
		self.FOV_s.clear() 	
		self.o_s.clear() 	
		self.remove_all_sprites()
		
		loader.load_objects(self.game, self.load_list, self.all_sprites)

	#<---- Projection Funcs
	def get_FOV_s(self):		
		self.c_t_s = None
		self.FOV_s.clear()
		self.o_s.clear()
	
		for i, s in enumerate(self.all_sprites):		
			if self.is_in_view(s):
				self.FOV_s.append((s.angle, s))
			s.hide()	
				
		if self.FOV_s:
			self.FOV_s.sort(key=lambda d: d[0], reverse=True)
			self.c_t_s = self.FOV_s[0][-1]
		
	def next_c_t_s(self):		
		self.c_t_s = None	
		self.FOV_s.pop(0)
		if self.FOV_s:
			self.c_t_s = self.FOV_s[0][-1]
			
	def update_sprites(self, dt):
		for i, s in enumerate(self.all_sprites):
			#if isinstance(s, DefaultAnimatedSprite) or isinstance(s, DefaultNPCSprite):
			s.update(dt)		
			
	def update(self, idx, dist, r_a):		
		if self.c_t_s and r_a < self.c_t_s.angle:
			
			if dist > self.c_t_s.d_f_player:
				self.o_s.append((self.c_t_s.d_f_player, self.c_t_s))
				self.c_t_s.project_on_screen(idx)
				
			self.next_c_t_s()

		if idx == NUMBER_OF_RAYS - 1:
			self.o_s.sort(key=lambda data: data[0], reverse=True)
			for i, s in enumerate(self.o_s):
				self.show_sprite(s[-1])
			
	def is_in_view(self, sprite):													
		p_angle = self.game.player.angle									    		
		p_x = self.game.player.pos_x
		p_y = self.game.player.pos_y							   
		
		Dx, Dy = sprite.pos_x - p_x, sprite.pos_y - p_y			
		max_angle, min_angle = p_angle + HALF_FOV, p_angle - HALF_FOV
		sprite.d_f_player = math.dist((sprite.pos_x, sprite.pos_y),(p_x, p_y))			   			   
		
		in_view = False
		if sprite.d_f_player < PLAYER_RADIUS:
			return in_view
						
		# Angle correction the hard way!
		if   Dx == 0 and Dy >= 0:
			sprite.angle = P_270_DEGREES
				
		elif Dx == 0 and Dy <  0:
			sprite.angle = P_90_DEGREES
			
		else:
			sprite.angle = math.atan(Dy/Dx)
			
			if   sprite.angle >= 0 and Dx > 0:
				sprite.angle = P_360_DEGREES - sprite.angle

			elif sprite.angle >= 0 and Dx < 0:
				sprite.angle = P_180_DEGREES - sprite.angle

			elif sprite.angle < 0 and Dx > 0:
				sprite.angle *= -1
				
			elif sprite.angle < 0 and Dx < 0:
				sprite.angle = P_180_DEGREES + math.fabs(sprite.angle)
	
			else:
				raise Exception('sprite_space.is_in_view() invalid angle!')

		# Check if within FOV
		if   P_90_DEGREES > p_angle >= ZERO_DEGREES and min_angle < 0:
			if   max_angle >= sprite.angle >= ZERO_DEGREES:
				in_view = True
				sprite.angle = sprite.angle
						
			elif P_360_DEGREES >= sprite.angle >= P_360_DEGREES + min_angle:
				in_view = True
				sprite.angle -= P_360_DEGREES
					
			else:
				in_view = False
		
		elif P_360_DEGREES >= p_angle > P_270_DEGREES and max_angle > P_360_DEGREES:
			if max_angle - P_360_DEGREES >= sprite.angle >= ZERO_DEGREES:
				in_view = True
				sprite.angle += P_360_DEGREES
							
			elif P_360_DEGREES >= sprite.angle >= min_angle:
				in_view = True
				sprite.angle = sprite.angle
						
			else:
				in_view = False
				
		else:
			 in_view = max_angle >= sprite.angle >= min_angle

		return in_view
		
	#<---- Events	
	def player_attack(self):
		max = self.game.player.angle + 0.1
		min = self.game.player.angle - 0.1
		
		for i, s in enumerate(self.o_s):			
			sprt = s[1]
			if isinstance(sprt, NPCSprite) and max >= sprt.angle >= min:
				if sprt.d_f_player < sprt.influence_range + random.uniform(0,1):
					sprt.receive_damage(self.game.player.atk_damage)	
		
	#<----Base Functions: re_init, update		
	def re_init(self, hide=_HIDE):
		super().re_init(hide)
		
		loader.init(self.game, self.load_list)

		self.reload_sprites()
				
