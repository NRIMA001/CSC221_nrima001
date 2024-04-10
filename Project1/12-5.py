import pygame

class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = 600, 400
        self.bg_color = (255, 255, 255)  
        
class KeyGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Key Game")

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    else:
                        print(event.key)
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    KeyGame().run_game()
