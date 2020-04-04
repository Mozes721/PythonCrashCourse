import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self,ai_settings, screen):
        super(Ball, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        #Load image
        self.image = pygame.image.load('Catch/ball_img.bmp')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.y += self.ai_settings.ball_speed
        self.rect.y = self.y
