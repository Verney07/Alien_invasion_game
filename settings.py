"""A class to setting up the background size and color."""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Mix of red, green and blue
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5  # pixel per cycle
        # Number of ships the player starts with.
        self.ship_limit = 3

        # Bullet settings: create a dark gray bullets.
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Limits the player to three bullets at a time.
        self.bullets_allowed = 3

        #Alien settings: alien's speed:
        self.alien_speed=1.0
        # Control the speed of the fleet drops down each time an alien reaches
        # either edge.
        self.fleet_drop_speed=10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction=1

