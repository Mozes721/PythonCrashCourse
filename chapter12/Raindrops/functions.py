import sys
import pygame
from rain_obj import Rain

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(ai_settings, screen, rain_drop):
    #put in variables in screen
    screen.fill(ai_settings.bg_color)
    #create a rain sprite loop
    for rain in rain_drop.sprites():
        #create new rain with the rain object
        new_rain = Rain(screen)
    #from the function call use raindropes as a placeholder/variable where it will update
    rain_drop.draw(screen)
    #update the screen status
    pygame.display.flip()

def create_rain(ai_settings, screen, rain_drop, rain_number):
    #create raindrop object at its location
    rain = Rain(screen)
    rain_width = rain.rect.width
    rain_height = rain.rect.height

    rain.x = rain_width + 2 * rain_width * rain_number
    rain.rect.x = rain.x
    rain_drop.add(rain)


def create_grid(ai_settings, screen, rain_drop):
    rain = Rain(screen)
    rain_width = rain.rect.width
    avalable_space_x = ai_settings.screen_width - 2 * rain_width
    number_rain_x = avalable_space_x // (2 * rain_width)
    for rain_number in range(number_rain_x):
        create_rain(ai_settings, screen, rain_drop, rain_number)
    ai_settings.new_grid = False

def rain_update(ai_settings, rain_drop):
    for raindrop in rain_drop.sprites():
        raindrop.y += ai_settings.rain_drop_speed
        raindrop.rect.y = raindrop.y
        if raindrop.rect.y >= ai_settings.screen_height:
            for raindrop in rain_drop.copy():
                rain_drop.remove(raindrop)
            ai_settings.new_grid = True
