import pygame.font
from pygame.sprite import Group
from catcher import Catcher
from ball import Ball

class Scoreboard():

    #class to report scorring info
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)




        self.prep_score()
        self.prep_high_score()
        self.prep_catchers()

    def prep_score(self):
        score_str = str(self.stats.score)
        rounder_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounder_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)


        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.high_score_rect.top

    def prep_catchers(self):
        self.balls = Group()
        for ball_numbers in range(self.stats.balls_left):
            ball = Ball(self.ai_settings, self.screen)
            ball.rect.x = 15 + ball_numbers * ball.rect.width
            ball.rect.y = 10
            self.balls.add(ball)

    def prep_level(self):
        """Turn the level into prep image"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        #Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.balls.draw(self.screen)
