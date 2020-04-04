import pygame
import sys
from rain_obj import Rain
from settings import Settings
import functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raindrops")
    rain_drop = Group()
    bg_color = (230,230,230)
    raindrops = Group()


    while True:
        gf.check_events()
        if ai_settings.new_grid:
            gf.create_grid(ai_settings, screen, rain_drop)
        gf.rain_update(ai_settings, rain_drop)
        gf.update_screen(ai_settings, screen, rain_drop)
run_game()
