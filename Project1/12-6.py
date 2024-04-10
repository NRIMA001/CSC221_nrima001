import pygame

class Bullet:
    def __init__(self, shooter):
        self.screen = shooter.screen
        self.settings = shooter.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = shooter.ship.rect.midright #position for the ship
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.bg_color = (230, 230, 230)
        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30 #limiting 30 bullets 
        self.ship_speed = 5

class Ship:
    def __init__(self, shooter):
        self.screen = shooter.screen
        self.settings = shooter.settings
        self.screen_rect = shooter.screen.get_rect()
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Shooter:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
        self.ship = Ship(self)
        self.bullets = []

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.append(new_bullet)

    def _update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
        self.bullets = [bullet for bullet in self.bullets if bullet.rect.left < self.screen.get_rect().right]

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    Shooter().run_game()
