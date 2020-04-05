import pygame
import sys
from settings import Settings
from pygame.sprite import Group
from ball import Ball
from catcher import Catcher
import catch_game_functions as gf
from game_active import GameStats
from scoreboard import Scoreboard



def run_game():

    #initialize background
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Ball catcher!")


    stats = GameStats(ai_settings)

    catcher = Group()
    baller = Group()

    #create an instance from store game statistics and create scoreboards
    sb = Scoreboard(ai_settings, screen, stats)




    while True:
        if stats.game_active:
            for c in catcher.sprites():
                gf.check_events(c)
        #update catcher
            gf.update_catcher(ai_settings, screen, catcher)
            #update baller
            gf.update_baller(ai_settings, stats, sb, screen, catcher, baller)

        gf.update_screen(ai_settings, screen, stats, sb, baller, catcher)




run_game()
