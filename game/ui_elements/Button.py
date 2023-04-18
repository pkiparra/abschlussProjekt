import pygame

from ui_elements.Colors import Colors


class Button:
    pygame.init()
    button_font = pygame.font.SysFont(None, 32)

    def __init__(self, x, y, width, height, title):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title

    def was_clicked(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print(self.title, "was clicked")
                return True

        return False

    def draw(self, screen, mousePos):
        
            if self.rect.collidepoint(mousePos):
                pygame.draw.rect(screen, Colors.BUTTON_HOVER_COLOR, self.rect)
            else:
                pygame.draw.rect(screen, Colors.BUTTON_COLOR, self.rect)
            text_surface = self.button_font.render(self.title, True, Colors.BUTTON_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

