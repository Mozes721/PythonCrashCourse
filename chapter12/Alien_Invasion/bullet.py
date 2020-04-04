import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        #creates a bullet object at ships current postion
        super(Bullet, self).__init__()
        self.screen = screen

        #create a bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_widht, ai_settings.bullet_height)
        #align the bullet to be in the center of ship object
        self.rect.centerx = ship.rect.centerx
        #set the rect top object and set it to top of the ship
        self.rect.top = ship.rect.top

        #store bullets value as decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        #move the bullet up to screen
        #make the object go in y axis with speed factor
        self.y -= self.speed_factor
        #asign bullet rect object to move in the y axis
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color, self.rect)
