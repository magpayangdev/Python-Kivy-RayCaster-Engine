
from scripts.bases.multi_rect_bases.base_minimap import BaseMinimap

class DefaultMinimap(BaseMinimap):
	def __init__(self, game, hide=True):
		super().__init__(game=game, hide=hide)
		
	def re_init(self, hide=True):
		super().re_init(hide=hide)
