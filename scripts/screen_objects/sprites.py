
from scripts.bases.base_sprites.animated_sprite import AnimatedSprite
from scripts.bases.base_sprites.static_sprite import StaticSprite
from scripts.bases.base_sprites.npc_sprite import NPCSprite
from scripts.bases.base_sprites.goal_sprite import BaseGoalSprite


class DefaultStaticSprite(StaticSprite):
	def __init__(self, game, sprite_id='flame', world_pos=(0,0), hide=True):
		super().__init__(game=game, sprite_id=sprite_id, minimap_icon='cherry.png', world_pos=world_pos,
						 radius=0.1, scale=0.5, health=10, influence_range=1, influence_amount=1, hide=hide)

class DefaultAnimatedSprite(AnimatedSprite):
	def __init__(self, game, sprite_id='flame', world_pos=(0,0), hide=True):	
		super().__init__(game=game, sprite_id=sprite_id, minimap_icon='fire.png', initial_mode='idle',
						 color=(1,1,1,1), world_pos=world_pos, scale=0.5, hide=hide, flip_time=0.1,
						 start_iter=True, health=10, speed=0, radius=0.1, influence_range=1, influence_amount=1)
			
class DefaultNPCSprite(NPCSprite):
	def __init__(self, game, sprite_id='soldier', world_pos=(0,0), hide=True):
		super().__init__(game, sprite_id=sprite_id, minimap_icon='monster.png', initial_mode='idle', 
						color=(1,1,1,1), world_pos=world_pos, scale=0.5, hide=hide, 
						idle_interval=0.5,walk_interval=0.5,hit_interval=0.2,die_interval=0.1,atk_interval=0.11, 
						health=2, speed=1, radius=0.1, attack_damage=1, attack_range=3, start_iter=True)

class GoalSprite(BaseGoalSprite):
	def __init__(self, game, sprite_id='candle_bra', world_pos=(0,0), hide=True):
		super().__init__(game=game, sprite_id=sprite_id, minimap_icon='cherry.png', world_pos=world_pos, 
					radius=0.1, scale=0.5, health=1, influence_range=0.40, influence_amount=1, hide=hide)