"""
player
"""

import math
import random
from settings import *


class Player:
	def __init__(self, game, pos_x = 1.5, pos_y = 1.5, angle = math.pi/2, radius = 0.1, health = 789, regen = 1):
		self.init_pos = pos_x, pos_y
		self.init_angle = angle
		self.init_health = health
		
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
		
		self.in_mmp_cnvs = False
		self.mmp_colour = None
		self.mmp_rect = None
		self.mmp_line = None
		
		self.is_moving_x, self.is_moving_y = False, False
		
		self.kill_list = []
		
	def add_to_kill_list(self, str):
		self.kill_list.append(str)
		
	def count_all_kills(self):
		d = dict()
		for str in self.kill_list:
			d[str] = d.get(str, 0) + 1		
		return d

	def re_init(self):
		self.pos_x, self.pos_y = self.init_pos
		self.angle = self.init_angle
		self.health = self.init_health
		self.kill_list.clear()
		self.event.player_health_updated()
	
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
		dx, dy, tx, ty = Player.move(dt, self.forward_dir, self.pos_x, self.pos_y, self.radius, self.angle, False)
		
		if self.game.graph_mngr.is_valid_position(tx, self.pos_y):
			self.pos_x += dx * self.max_walk_speed
			self.is_moving_x = True
		else:
			self.is_moving_x = False
		
		if self.game.graph_mngr.is_valid_position(self.pos_x, ty):
			self.pos_y += dy * self.max_walk_speed
			self.is_moving_y = True
		else:
			self.is_moving_y = False
			
		self.speed = math.dist((0,0),(dx * self.max_walk_speed, dy * self.max_walk_speed))
		
	def move_right(self, dt):	
		dx, dy, tx, ty = Player.move(dt, self.right_dir, self.pos_x, self.pos_y, self.radius, self.angle, True)
												 			
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