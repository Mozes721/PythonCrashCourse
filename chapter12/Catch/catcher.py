import pygame
from pygame.sprite import Sprite
class Catcher(Sprite):

    def __init__(self,ai_settings, screen):

        super(Catcher, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('Catch/catcher_img.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self, ai_settings, screen):
        """Update catcher position."""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += ai_settings.catcher_speed_factor
        if self.moving_left and self.rect.left >= 0:
            self.center -= ai_settings.catcher_speed_factor
        self.rect.centerx = self.center

    def center_catcher(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)
