import pygame, registration_view

from ui_elements.Button import Button
from ui_elements.Colors import Colors

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_SPACING = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ai mini games")

headline_font = pygame.font.SysFont(None, 64)
headline_text = "Ai mini games"
button_texts = ["Login", "Registrieren", "Als Gast spielen"]

headline_surface = headline_font.render(headline_text, True, Colors.HEADLINE_COLOR)
headline_rect = headline_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))

buttons = []
for i, text in enumerate(button_texts):
    x = SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2
    y = 150 + i * (BUTTON_HEIGHT + BUTTON_SPACING)
    buttons.append(Button(x, y, BUTTON_WIDTH, BUTTON_HEIGHT, text))

def start_app():
    screen.fill(Colors.BACKGROUND_COLOR)
    screen.blit(headline_surface, headline_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:        
                for button in buttons:
                    if button.was_clicked(event):
                        if button.title == "Registrieren":
                            registration_view.draw_view(screen)
        for button in buttons:                    
            button.draw(screen, pygame.mouse.get_pos())

        pygame.display.update()