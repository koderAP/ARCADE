import pygame
from settings import WIDTH, HEIGHT

class DialogBox:
    def __init__(self, x, y, width, height, background_image, text, font):
        self.background_image = pygame.image.load(background_image).convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font

    def render(self, surface):
        surface.blit(self.background_image, (self.rect.x, self.rect.y))
        
        lines = self.text.split('\n')
        y = HEIGHT - 150
        for line in lines:
            text_surface = self.font.render(line, True, (0, 0, 0))
            text_rect = text_surface.get_rect(left=100, top=y)
            surface.blit(text_surface, text_rect)
            y += 30


    def set_text(self, text):
        self.text = text