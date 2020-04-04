import sys

import pygame

def check_events(cat):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cat.moving_right = True
            elif event.key == pygame.K_LEFT:
                cat.moving_left = True
            elif event.key == pygame.K_UP:
                cat.moving_up = True
            elif event.key == pygame.K_DOWN:
                cat.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                cat.moving_right = False
            elif event.key == pygame.K_LEFT:
                cat.moving_left = False
            elif event.key == pygame.K_UP:
                cat.moving_up = False
            elif event.key == pygame.K_DOWN:
                cat.moving_down = False

def update_screen(ai_settings, screen, cat):
    screen.fill(ai_settings.bg_color)
    cat.blitme()

    pygame.display.flip()
