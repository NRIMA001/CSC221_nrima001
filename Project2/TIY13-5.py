from random import randint, random
import pygame
from pygame.sprite import Sprite
import sys


class Alien(Sprite):
    """ Alien class to represent aliens"""
    def __init__(self, ss_game):
        # Initialize alien and set its position
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.image = pygame.image.load('alien1.png')
        self.rect = self.image.get_rect()
        self.rect.left = self.screen.get_rect().right
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)
        self.x = float(self.rect.x)

    def update(self):
        # Update the alien's position
        self.x -= self.settings.alien_speed
        self.rect.x = self.x


class Bullet(Sprite):
    """Bullet class to manage bullets"""
    def __init__(self, ss_game):
        # Create a bullet 
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midright = ss_game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Settings:
    """Settings class to store all game settings"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3.0
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_frequency = 0.008
        self.alien_speed = 1.5

class Ship:
    """ Ship class to manage the ship"""
    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()
        self.image = pygame.image.load('sideship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Update the ship's position
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class SidewaysShooter:
    "Sideways Shooter Game for Alien Invasion"
    def __init__(self):
        # Initialize the game
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self._create_alien()
            self.ship.update()
            self._update_bullets()
            self.aliens.update()
            self._update_screen()

    def _check_events(self):
        # Check for keypresses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Respond to keypresses
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # Update bullet positions and check for collisions
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

    def _create_alien(self):
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)
            print(len(self.aliens))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ss_game = SidewaysShooter()
    ss_game.run_game()
