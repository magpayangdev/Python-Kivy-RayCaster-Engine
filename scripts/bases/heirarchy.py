
LayoutBase # layout (widget)
|
------SpritesContainer
		|
		------ScreenSpritesSpace # Non implemented
		|
		------SceneSpritesSpace # Micro-manages scene sprites, e.g. in_view, angles, show, remove and delete sprite ... etc


Base
|
------WindowObjects # window, in_cnvs, re_size, show, hide, remove
|		|                    
|		------RectBase
|		|		|
|		|		------TexturedRect  
|		|		|
|		|		------SequenceTexturedRect
|		|	
|		------TextBase
|		|
|		------ButtonBase
|				|
|				------DropDownBase
|		
------TimedUpdate # accum_time, flip_time, do_once, fbf_update, timed_update, do_once_func, stop_iteration
|		|
|		------TimedRect
|		|
|		------TimedTexture 
|		|		|
|		|		------Sky +
|		|		|
|		|		------Floor +
|		|
|		------TimedImageSequence
|		|		|
|		|		------ScreenSprite
|		|		|		|
|		|		|		------PlayerSprite +
|		|		|
|		|		------SceneSprite # Sprites that are projected on screen and drawn on game.sprite_space.canvas
|		|				|						
|		|				------StaticSprite + 
|		|				|		|
|		|				|		------GoalSprite
|		|				|
|		|				------AnimatedSprite +
|		|				|
|		|				------NPCSprite +
|		|
|		------TimedQuadrant 
|				|
|				------UserHud + 
|
------TouchObjects
		|
		------CardManager 
		|
		------QuadrantTouchObject # Touch Events are divided into four quadrants
				|
				------HudBase


Applied Bases

1. Cards # A RectBase that spawns a TexturedRect as image_comp, TextBase as text_comp and ButtonBase as button_comp
		|
		------LoadingScreen ?
		|
		------MenuCard +
		|
		------ScoreCard
		|
		------TypingCard + 
	

2. MultiRectBase # Mass spawns RectBase 
		|
		------ArrayRect # Rects are arranged linearly
		|		|
		|		------DigitalCounter
		|				|
		|				------DefaultHealthIndicator
		|
		------NestedRect # Rects are nested
		|		|
		|		------BaseController
		|				|
		|				------LeftController +
		|				|
		|				------RightController +
		|
		------Grid  # Rects are on a grid
		|		|
		|		------BaseMinimap
		|
		------Walls # Rects are positioned based on ray index and distance from player 
				|	
				------World +
				