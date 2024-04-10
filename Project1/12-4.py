import pygame

class Rocket:
    def __init__(self, r_game):
        self.screen, self.settings = r_game.screen, r_game.settings
        self.screen_rect = r_game.screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load("rrocket.webp").convert_alpha(), (160, 160))  
        self.rect = self.image.get_rect() 
        self.rect.center = self.screen_rect.center  
        self.x, self.y = float(self.rect.x), float(self.rect.y) 
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False


    def update(self):
        dx = self.settings.rocket_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += dx
        if self.moving_left and self.rect.left > 0:
            self.x -= dx
        if self.moving_up and self.rect.top > 0:
            self.y -= dx
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += dx
        self.rect.x, self.rect.y = self.x, self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = 800, 600
        self.bg_color = (135, 206, 250)  # Changing the background color to blue
        self.rocket_speed = 10

class RocketGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")
        self.rocket = Rocket(self)
        self.running = True

    def run_game(self):
        while self.running:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_key_events(event, True)
            elif event.type == pygame.KEYUP:
                self._check_key_events(event, False)

    def _check_key_events(self, event, is_pressed):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = is_pressed
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = is_pressed
        if event.key == pygame.K_UP:
            self.rocket.moving_up = is_pressed
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = is_pressed
        elif event.key == pygame.K_q:
            self.running = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    RocketGame().run_game()
