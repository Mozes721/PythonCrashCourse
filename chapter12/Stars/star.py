import pygame
from pygame.sprite import Sprite 

class Star(Sprite):
    """Models star object"""
    def __init__(self, ai_settings, screen):
        super(Star, self).__init__()
        self.screen = screen 
        #load the star image
        self.image = pygame.image.load('/Users/richard/Desktop/PythonCrashCourse/chapter12/Stars/star.bmp')
        self.rect = self.image.get_rect()

        #Set star rect at top left position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save exact postion of the star
        self.x = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image, self.rect)

