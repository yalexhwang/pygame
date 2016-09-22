import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings):
		super(Bullet, self).__init__()
		# or Sprite.__init__(self)
		self.screen = screen

		#Make a bullet 
		self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
		self.rect.centerx = hero.rect.centerx
		self.rect.top = hero.rect.top
		self.color = game_settings.bullet_color
		self.speed = game_settings.bullet_speed
		self.y = self.rect.y

	def update(self):
		#every time update is run, move the bullet go up (y-axis)
		self.y -= self.speed
		self.rect.y = self.y #update rect position

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		