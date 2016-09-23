import pygame
import random
from pygame.sprite import Sprite

class Monster(Sprite):
	def __init__(self, screen):
		super(Monster, self).__init__()
		self.screen = screen

		#randomize monster specs
		self.level = random.randint(1, 5)
		self.speed = random.randint(2, 20)
		self.direction = random.randint(0, 1)

		#randomize monster images
		img = ['m-black.png', 'm-purple.png', 'm-boss.png', 'm-octopus.png', 'm-tongue.png', 'm-tyrano.png']
		img_i = random.randint(0, len(img) - 1)
		self.image = pygame.image.load('images/' + img[img_i])
	
		#randomize monster destinations		
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object so we  ~~
		self.screen_rect = screen.get_rect()
		def monster_dest():
			dest = random.randint(self.screen_rect.left, self.screen_rect.right)
			return dest
		self.rect.centerx = monster_dest()
		self.rect.top = self.screen_rect.top
		print self.rect.left 
		print self.rect.right

	def update(self):
		def monster_move(speed, direction, level):
			def random_change(level):
				chance = 0
				if level == 3:
					chance = random.randint(1,5)
				elif level == 2:
					chance = random.randint(1,9)
				elif level == 1:
					chance = 0
				return chance

			if direction == 1:
				if self.rect.right >= self.screen_rect.right:
					self.direction = 0
				else:
					self.rect.right += speed 
					if random_change(level) == 1:
						self.direction = 0
 			else:
				if self.rect.left <= self.screen_rect.left:
					self.direction = 1
				else:
					self.rect.right -= speed
					if random_change(level) == 1:
						self.direction = 1

			

		monster_move(self.speed, self.direction, self.level)


	def draw_monster(self):
		self.screen.blit(source = self.image, dest = self.rect)