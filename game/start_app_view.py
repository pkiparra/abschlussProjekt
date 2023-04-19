import pygame, registration_view, login_View, choose_game_view
from classes import User
from ui_elements.Button_types import Button_types
from ui_elements.Button import Button
from ui_elements.Colors import Colors

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_SPACING = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ai mini games")

headline_font = pygame.font.SysFont(None, 64)
headline_text = "Ai mini games"
button_texts = [Button_types.LOGIN, Button_types.SIGNUP, Button_types.PLAY_AS_GUEST]

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
                        if button.title == Button_types.SIGNUP:
                            registration_view.draw_view(screen)
                        if button.title == Button_types.LOGIN:
                            login_View.draw_view(screen)
                        if button.title == Button_types.PLAY_AS_GUEST:
                            user = User()
                            choose_game_view.draw_view(screen, user)
        for button in buttons:                    
            button.draw(screen, pygame.mouse.get_pos())

        pygame.display.update()