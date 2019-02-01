import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __int__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position."""
		super().__int__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the aliend image and set its rect attribute.
		self.image = pygame.image.load('image/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact position.
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blitme(self.image, self.rect)
