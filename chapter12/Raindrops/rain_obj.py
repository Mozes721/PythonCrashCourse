import pygame

from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self, screen):
        super(Rain,self).__init__()
        self.screen = screen

        self.image = pygame.image.load('chapter12/Raindrops/raindrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def blitme(self):
        self.screen.blit(self.image, self.rect)
