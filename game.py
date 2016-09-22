import pygame #imports package with all available pygame modules
from hero import Hero #bring in the hero class with all it's methods and glory
from settings import Settings
import game_functions as gf
from pygame.sprite import Group, groupcollide
from bullets import Bullet 
from monster import Monster

#Set up the main core function
def run_game():
  pygame.init() #initializes pygame modules
  #create an instance of Settings class and assign it to game_settings
  game_settings = Settings()
  #set screen size, need double parenthesis, or set width and height to variable
  screen = pygame.display.set_mode(game_settings.screen_size)
  #set msg on status bar
  pygame.display.set_caption("Monster Attack")

  #set variable equal to the class and pass it to the screen
  hero = Hero(screen) 

  #set the bullets to group(built-in of pygame, upgrade to list)
  bullets = Group()
  monsters = Group()

  while 1: #1 is true, run this loop forever...
    #call gf (aliased from game_functions), get the check_event method
    gf.check_events(hero, bullets, monsters, screen, game_settings) 
    hero.update() #update the hero flags
    bullets.update() 
    monsters.update()
    #call to update the screen
    gf.update_screen(game_settings, screen, hero, bullets, monsters)
    #get rid of bullets that are off the screen
    groupcollide(bullets, monsters, True, True)



run_game() #start the game




