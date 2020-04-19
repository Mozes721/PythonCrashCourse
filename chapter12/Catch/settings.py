class Settings():

    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230, 230)

        #ball Settings
        self.ball_speed = 1

        #catcher settings
        self.catcher_speed_factor = 2

        #game settings
        self.ball_limit = 3

        self.catch_points = 50

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the ailein point increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.catcher_speed_factor = 2
        self.ball_speed = 1.5


    def increase_speed(self):
        self.catcher_speed_factor *= self.speedup_scale
        self.ball_speed *= self.speedup_scale

        self.catch_points = int(self.catch_points * self.score_scale)
