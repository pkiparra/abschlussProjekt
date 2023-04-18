import pygame

from ui_elements.Colors import Colors


class TextInput:
    pygame.init()
    FONT = pygame.font.SysFont(None, 30)
    def __init__(self, x, y, width, height, title):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.text = ""
        self.selected = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = True
            else:
                self.selected = False
        elif event.type == pygame.KEYDOWN and self.selected:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        if self.selected:
            pygame.draw.rect(screen, Colors.BUTTON_HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(screen, Colors.BUTTON_COLOR, self.rect)
  
        title_text = self.FONT.render(self.title, False, Colors.HEADLINE_COLOR)
        title_text_rect = title_text.get_rect()
        title_text_rect.x = self.rect.x + 10
        title_text_rect.y = self.rect.y - title_text_rect.height -5
        screen.blit(title_text, title_text_rect)

        input_text = self.FONT.render(self.text, False, Colors.BUTTON_TEXT_COLOR)
        input_text_rect = input_text.get_rect()
        input_text_rect.x = self.rect.x + 10
        input_text_rect.y = self.rect.y + 10
        screen.blit(input_text, input_text_rect)
