import pygame
from ui_elements.Button_types import Button_types
from ui_elements.Colors import Colors

class Button:
    pygame.init()

    def __init__(self, x, y, width, height, title: Button_types, font_size = 32):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.font_size = font_size
        self.button_font = pygame.font.SysFont(None, self.font_size )

    def was_clicked(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print(self.title.value, "was clicked")
                return True

        return False

    def draw(self, screen, mousePos):
        
            if self.rect.collidepoint(mousePos):
                pygame.draw.rect(screen, Colors.BUTTON_HOVER_COLOR, self.rect)
            else:
                pygame.draw.rect(screen, Colors.BUTTON_COLOR, self.rect)
            text_surface = self.button_font.render(self.title.value, True, Colors.BUTTON_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

