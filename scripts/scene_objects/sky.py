
from scripts.bases.base_sky import BaseSky

_HIDE = True


class DefaultSky(BaseSky):
	def __init__(self, game, sky_path, **kwargs):
		super().__init__(game=game, image_name=sky_path, hide=_HIDE)
		
	def re_init(self, sky_path, **kwargs):
		super().re_init(image_name=sky_path, hide=_HIDE)