#Place all main game functions here, to keep things compartmentalized
import sys
import time
import pygame
from bullets import Bullet
from monster import Monster


def check_events(hero, bullets, monsters, screen, game_settings, play_button):
  #run through all pygame events
  for event in pygame.event.get():
    #...if it's QUIT, exit the game
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if play_button.rect.collidepoint(mouse_x, mouse_y):
          game_settings.game_active = True
    elif event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_RIGHT: #righ pressed
        hero.moving_right = True #set the flag
      elif event.key == pygame.K_LEFT:
        hero.moving_left = True #set the flag to move the hero
      elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, hero, game_settings)
        bullets.add(new_bullet)
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        hero.moving_right = False
      elif event.key == pygame.K_LEFT:
        hero.moving_left = False


def update_screen(settings, screen, hero, bullets, monsters, play_button):
  screen.fill(settings.bg_color) #fill the background(bg) with our green
  hero.draw_me() #call the draw method and put the hero on the screen
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  for monster in monsters.sprites():
    monster.draw_monster()
  if not settings.game_active:
    play_button.draw_button()
  if len(monsters) == 0:
    settings.game_active = False
  pygame.display.flip()

