import sys
import pygame
from random import randint
from pygame.sprite import Sprite
from settings import Settings

class Star(Sprite):
    """A class to represent a single star."""
    def __init__(self, screen, star_image):
        super().__init__()
        self.screen = screen
        self.image = star_image
        self.rect = self.image.get_rect()

        # Set random position within the screen boundaries
        self.rect.x = randint(0, screen.get_width() - self.rect.width)
        self.rect.y = randint(0, screen.get_height() - self.rect.height)


class StarsGame:
    """Stars on the sky"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        # Load star image
        self.star_image = pygame.image.load('star.png')

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        num_stars = 68  # number of star
        # Create stars
        for _ in range(num_stars):
            star = Star(self.screen, self.star_image)
            self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    sg = StarsGame()
    sg.run_game()
