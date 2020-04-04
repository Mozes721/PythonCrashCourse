import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        #initialize screen and starting possition
        self.screen = screen
        #load the image im pygame
        self.ai_settings = ai_settings

        self.image = pygame.image.load("chapter12/Alien_Invasion/ship_img.bmp")
        #set the image in rect
        self.rect = self.image.get_rect()
        #set screen rect
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #moving states of ship
        self.moving_right = False
        self.moving_left = False



    def update(self):
        #update the ships position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor


        #update rect object from self.center
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)