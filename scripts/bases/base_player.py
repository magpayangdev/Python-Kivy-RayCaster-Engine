
""" player """

import math
import random
from settings import *

_PX, _PY, _A, _R, _H, _REGEN = 1.5, 1.5, 0, 0.1, 789, 1 


class BasePlayer:
	def __init__(self, game, pos_x=_PX, pos_y=_PY, angle=_A, radius=_R, health=_H, regen=_REGEN):	
		self.game = game
		self.event = self.game.event
		self.accum_time = 0
		
		self.pos_x, self.pos_y = pos_x, pos_y
		self.angle = angle
		self.health = health
		self.regen = regen
		
		self.atk_damage = 1

		self.radius = radius
		self.forward_dir = 0
		self.right_dir = 0
		self.yaw = 0
		self.max_walk_speed = 2
		self.turn_speed = 2
		self.speed = 0
		
		self.kill_list = []

	def re_init(self, pos_x=_PX, pos_y=_PY, angle=_A, radius=_R, health=_H, regen=_REGEN):
		self.accum_time = 0
		
		self.pos_x, self.pos_y = pos_x, pos_y
		self.angle = angle
		
		self.health = health
		self.regen = regen
		
		self.atk_damage = 1

		self.radius = radius
		self.forward_dir = 0
		self.right_dir = 0
		self.yaw = 0
		self.max_walk_speed = 2
		self.turn_speed = 2
		self.speed = 0
		
		self.kill_list = []
		
	def add_to_kill_list(self, str):
		self.kill_list.append(str)
		
	def count_all_kills(self):
		d = dict()
		for str in self.kill_list:
			d[str] = d.get(str, 0) + 1		
		return d

	
	def hit(self, damage_amount=10):
		self.health = max(0, min(MAX_PLAYER_HEALTH, self.health - damage_amount))
		return self.health
		
	def update(self, dt):
		self.move_forward(dt)
		self.move_right(dt)
		self.look_right(dt)
		
		self.accum_time += dt
		if self.accum_time > self.regen: #<---- Regen
			self.accum_time = 0
			self.health = max(0, min(MAX_PLAYER_HEALTH, self.health + 1))

			self.event.player_health_updated()
	
	def move_forward(self, dt):
		dx, dy, tx, ty = BasePlayer.move(dt, self.forward_dir, self.pos_x, self.pos_y, self.radius, self.angle, False)
		
		if self.game.graph_mngr.is_valid_position(tx, self.pos_y):
			self.pos_x += dx * self.max_walk_speed
		else:
			pass
		
		if self.game.graph_mngr.is_valid_position(self.pos_x, ty):
			self.pos_y += dy * self.max_walk_speed
		else:
			pass
			
		self.speed = math.dist((0,0),(dx * self.max_walk_speed, dy * self.max_walk_speed))
		
	def move_right(self, dt):	
		dx, dy, tx, ty = BasePlayer.move(dt, self.right_dir, self.pos_x, self.pos_y, self.radius, self.angle, True)
												 			
		if self.game.graph_mngr.is_valid_position(tx, self.pos_y):
			self.pos_x += dx * self.max_walk_speed
		
		if self.game.graph_mngr.is_valid_position(self.pos_x, ty):
			self.pos_y += dy * self.max_walk_speed	
	
	def look_right(self, dt):
		self.angle -= dt * self.yaw * self.turn_speed #<--- yaw
		#self.angle -= dt * 0.1 * self.turn_speed
		
		if self.angle < 0:
			self.angle += 2 * math.pi 
		
		if self.angle > 2 * math.pi:
			self.angle -= 2 * math.pi
	
	@staticmethod
	def move(dt, value, pos_x, pos_y, radius, angle , strafe=False):
		if value == 0:
			return 0, 0, 0, 0 
			
		if strafe:
			cosine_theta, sine_theta =  math.sin(angle), -math.cos(angle)
		else:
			cosine_theta, sine_theta = math.cos(angle), math.sin(angle)
		
		dx, dy = cosine_theta * dt * value, - sine_theta * dt * value
			
		if value > 0:		
			if cosine_theta > 0 and sine_theta > 0:
				tx = pos_x + radius + dx
				ty = pos_y - radius + dy
			
			elif cosine_theta < 0 and sine_theta > 0:
				tx = pos_x - radius + dx
				ty = pos_y - radius + dy
				
			elif cosine_theta < 0 and sine_theta < 0:
				tx = pos_x - radius + dx
				ty = pos_y + radius + dy
				
			elif cosine_theta > 0 and sine_theta < 0: 
				tx = pos_x + radius + dx
				ty = pos_y + radius + dy
			
			elif cosine_theta == 0:
				tx = pos_x + radius
				if sine_theta >= 0:
					ty = pos_y - radius + dy
				else:
					ty = pos_y + radius + dy 
			
			elif sine_theta == 0:
				ty = pos_y + radius
				if cosine_theta >= 0:
					tx = pos_x + radius + dx
				else:
					tx = pos_x - radius + dx
	
		elif value < 0:
			if cosine_theta > 0 and sine_theta > 0:
				tx = pos_x - radius + dx
				ty = pos_y + radius + dy
				
			elif cosine_theta < 0 and sine_theta > 0:
				tx = pos_x + radius + dx
				ty = pos_y + radius + dy
				
			elif cosine_theta < 0 and sine_theta < 0:
				tx = pos_x + radius + dx
				ty = pos_y - radius + dy
				
			elif cosine_theta > 0 and sine_theta < 0:
				tx = pos_x - radius + dx
				ty = pos_y - radius + dy
				
			elif cosine_theta == 0:
				tx = pos_x + radius
				if sine_theta >= 0:
					ty = pos_y + radius + dy
				else:
					ty = pos_y - radius + dy 
			
			elif sine_theta == 0:
				ty = pos_y + radius
				if cosine_theta >= 0:
					tx = pos_x - radius + dx
				else:
					tx = pos_x + radius + dx
				
		else:
			return 0, 0, 0, 0
			
		return dx, dy, tx, ty