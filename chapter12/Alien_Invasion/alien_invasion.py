import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


#imported instances are set before the while loop
def run_game():
    #initialize background settings for pygame
    pygame.init()
    #create instance of settings
    ai_settings = Settings()
    #set display mode
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #place text
    pygame.display.set_caption("Alien Invasion!!!")
    #Make play button
    play_button = Button(ai_settings, screen, "Play")
    #make a stats instance to store game statistis
    stats = GameStats(ai_settings)
    #make a ship instance and use the screen value from settings

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    #make a group to store bullets
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    #create an instance from store game statistics and create scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    bg_color = (230,230,230)
    #write a loop of game
    #here the instances of other files will be used for the game functionality
    while True:
        #from ship instance use blitme function to call it in the screen
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats,sb, screen, ship, aliens, bullets)
        #every time you exit the loop update with recent changes by using pygame.display.flip() etc
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

#run game/function
run_game()
