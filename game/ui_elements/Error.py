import pygame

from ui_elements.Colors import Colors



class Error:
    pygame.init()
    button_font = pygame.font.SysFont(None, 32)

    def __init__(self, x, y, width, height, title):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.isVisible = True

    def draw(self, screen):
            pygame.draw.rect(screen, Colors.ERROR_COLOR, self.rect)
            
            text_surface = self.button_font.render(self.title, True, Colors.BUTTON_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)