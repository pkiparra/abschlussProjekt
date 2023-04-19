import pygame

from ui_elements.Button_types import Button_types
from ui_elements.Colors import Colors
from classes import User
from ui_elements.Button import Button


class Stay_clicked_button(Button):
    pygame.init()

    def __init__(self, x, y, width, height, title: Button_types, font_size = 32):
        super().__init__( x, y, width, height, title, font_size)
        self.can_stay_clicked: bool = False

    def draw(self, screen, mousePos, currently_selected: str):
        
            if self.rect.collidepoint(mousePos):
                pygame.draw.rect(screen, Colors.BUTTON_HOVER_COLOR, self.rect)
            elif self.title.value == currently_selected:
                pygame.draw.rect(screen, Colors.BUTTON_HOVER_COLOR, self.rect)
            else:
                pygame.draw.rect(screen, Colors.BUTTON_COLOR, self.rect)

            text_surface = self.button_font.render(self.title.value, True, Colors.BUTTON_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

