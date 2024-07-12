"""A class to setting up the background size and color."""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Mix of red, green and blue
        self.bg_color = (230, 230, 230)

        # Number of ships the player starts with.
        self.ship_limit = 3

        # Bullet settings: create a dark gray bullets.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Limits the player to three bullets at a time.
        self.bullets_allowed = 3

        # Alien settings: Control the speed of the fleet drops down 
        # each time an alien reaches either edge.
        self.fleet_drop_speed=10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        # Initialize the values for attributes that need to change throughout
        # the game.
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Ship settings
        self.ship_speed = 1.5  # pixel per cycle
        self.bullet_speed = 2.5
        #Alien settings: alien's speed:
        self.alien_speed=1.0
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction=1

        # Scoring settings: alien's point value.
        self.alien_points = 50

    def increase_speed(self):
        """
        Increase speed settings eahc time the player reaches a new level
        and alien point value.
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # Increase alien point value: use the 'int' function to increase
        # the point value by whole integers.
        self.alien_points = int(self.alien_points * self.score_scale)

