import pygame

class Hero(object):
	def __init__(self, screen):
		#give the hero the ability to control the screen
		self.screen = screen 

		#Load the hero image, get its rect
		self.image = pygame.image.load('images/hero.png')
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object so we  ~~
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving_right = False #set up movement booleans
		self.moving_left = False
	
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 10 
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= 10

	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect)