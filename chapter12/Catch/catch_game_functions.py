import sys
import pygame
from ball import Ball
from time import sleep
from pygame.sprite import Sprite
from catcher import Catcher
from random import randint
from os import path
import shelve



def check_events(catcher):
    """Cactch keyboard presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)


def check_keydown_events(event, catcher):
    """Check for key press events."""
    if event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, catcher):
    """Check for key release events."""
    if event.key == pygame.K_LEFT:
        catcher.moving_left = False
    elif event.key == pygame.K_RIGHT:
        catcher.moving_right = False


def update_catcher(ai_settings, screen, catcher):
    #get the rect screen position so can insert catcher_img
    screen_rect = screen.get_rect()
    catcher.update(ai_settings, screen)
    if len(catcher) == 0:
        # make a c variabe insantiate Catcher screen
        c = Catcher(ai_settings, screen)
        #at first center the catcher at screen centerx
        c.center = screen_rect.centerx
        #then the catcher rect centerx should align with c.center because have to user rect to insert the img
        c.rect.centerx = c.center
        #same center the rect_img bottom at screen bottom
        c.rect.bottom = screen_rect.bottom
        #add the catcher value from function and append the c class
        catcher.add(c)

def update_baller(ai_settings, stats, sb, screen, catcher, baller):
    screen_rect = screen.get_rect()
    baller.update()
    #function to check if the ball hit the bottom
    check_ball_bottom(stats, sb, screen_rect, baller)
    #check the lenghts of the ball
    if len(baller) == 0:
        new_b = Ball(ai_settings, screen)
        #randomly create a rand ball position
        new_b.x = randint(new_b.rect.width, screen_rect.right - new_b.rect.width)
        # put the new ball as x rect img
        new_b.rect.x = new_b.x
        #the height set up
        new_b.y = new_b.rect.height
        # put the new ball as y rect img
        new_b.rect.y = new_b.y
        #add the ball
        baller.add(new_b)
    elif stats.balls_left == 0:
        stats.game_active = False

    #set the collision possibility
    collision = pygame.sprite.groupcollide(baller, catcher, True, False)
    cheked = 0
    if collision:
        cheked += 1
        for baller in collision.values():
            stats.score += ai_settings.catch_points * len(baller)
            sb.prep_score()
            chech_high_score(stats, sb)
            if cheked == 3:
                ai_settings.increase_speed()
                stats.level +=1
                sb.prep_level()
                cheked = 0


def chech_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score


def update_screen(ai_settings, screen,stats, sb, baller, catcher):
    sb.prep_high_score()

    screen.fill(ai_settings.bg_color)
    #draw the score information
    sb.show_score()
    catcher.draw(screen)
    baller.draw(screen)
    pygame.display.flip()

def check_ball_bottom(stats, sb, screen_rect, baller):
    #make a for loop copy the ball
    for b in baller.copy():
        if b.rect.top >= screen_rect.bottom:
            baller.remove(b)
            stats.balls_left -= 1
            sb.prep_catchers()
            sleep(1.5)
