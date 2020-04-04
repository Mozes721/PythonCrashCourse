import sys, os
from settings import Settings
from os import path


class GameStats(object):
    """Track game statistics."""

    def __init__(self, ai_settings):
        """Initialize game statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.load_data()
        # Game active flag.
        self.game_active = True


    def load_data(self):
        #load the high score
        try:
            self.high_score_file = open('/Users/richard/Desktop/PythonCrashCourse/chapter12/high_score.txt', 'r+')
            self.high_score = str(self.high_score_file.read())
            self.high_score.close()
        except:
            self.high_score = 0

    def reset_stats(self):
        """
        Initialize game statistics which can change during game play.
        """
        self.balls_left = self.ai_settings.ball_limit
        self.score = 0
