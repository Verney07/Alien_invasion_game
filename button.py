"""Import the 'pygame.font' module to render text to the screen."""
import pygame.font

class Button:
    """A class to build buttons for the game."""
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)     #dark green background
        self.text_color = (255, 255, 255)   # text in white
        
        # Prepare a 'font' attribute for rendering text.
        # None==>'default font'; size text =48
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)      

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # The 'msg' parameter will be rendered as an image.
        # 'font.render()' turns the text into an image.
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blank button and then draw message."""
        # Draw the rectangular portion of the button.
        self.screen.fill(self.button_color, self.rect)
        # Draw the text image to the screen.
        self.screen.blit(self.msg_image, self.msg_image_rect)
       