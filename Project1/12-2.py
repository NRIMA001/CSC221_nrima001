import pygame
import sys

class Character:
    def __init__(self, image_path, screen_width, screen_height, background_color):
        self.image = pygame.image.load(image_path).convert_alpha() 
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.background_color = background_color

    def draw(self, surface):
        surface.fill(self.background_color)
        surface.blit(self.image, self.rect)

def main():

    pygame.init()

    width, height = 800, 600
    BLUE = (135, 206, 250)  

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Please Work")
    character = Character("santa.png", width, height, BLUE) 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        character.draw(window)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

