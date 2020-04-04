import pygame
from cat_obj import Cat
from settings2 import Settings
import game_function as gf

def run_game():

    pygame.init()
    ai_settings = Settings(cat_speed_factor = 1.5)

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("FISH HUNT!!!")

    bg_color = (35, 130, 215)
    cat = Cat(ai_settings, screen)


    while True:
        gf.check_events(cat)
        cat.update()
        gf.update_screen(ai_settings, screen, cat)
        screen.fill(bg_color)
        cat.blitme()
        pygame.display.flip()

run_game()
