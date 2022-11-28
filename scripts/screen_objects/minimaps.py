
from scripts.bases.applied_bases.base_minimap import BaseMinimap

class DefaultMinimap(BaseMinimap):
	def __init__(self, game, hide=True):
		super().__init__(game=game, hide=hide)
