import sys, os
from settings import Settings
from os import path
import shelve

class GameStats(object):
    """Track game statistics."""

    def __init__(self, ai_settings):
        """Initialize game statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Game active flag.
        self.game_active = True
        self.high_score = 0



    def reset_stats(self):
        """
        Initialize game statistics which can change during game play.
        """
        self.balls_left = self.ai_settings.ball_limit
        self.score = 0
        self.level = 1
