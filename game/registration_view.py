import pygame, start_app_view
from ui_elements.Colors import Colors
from ui_elements.Button import Button
from ui_elements.TextImput import TextInput

pygame.init()

TEXT_AND_BUTTON_WIDTH = 250
TEXT_AND_BUTTON_HEIGHT = 50
TEXT_AND_BUTTON_SPACING = 50

headline_font = pygame.font.SysFont(None, 64)
button_font = pygame.font.SysFont(None, 32)
headline_text = "Ai mini games"
button_text = "Als Gast spielen"
text_input_titles = ["username", "Passwort", "Passwort wiederholen"]

def draw_view(screen):
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()

    input_fields = []
    for i, text in enumerate(text_input_titles):
        x = SCREEN_WIDTH // 2 - TEXT_AND_BUTTON_WIDTH // 2
        y = 150 + i * (TEXT_AND_BUTTON_HEIGHT + TEXT_AND_BUTTON_SPACING)
        input_fields.append(TextInput(x, y, TEXT_AND_BUTTON_WIDTH, TEXT_AND_BUTTON_HEIGHT, text))
    
    buttons = []
    buttons.append(Button(10, 10, 40, 40, "<"))
    x = SCREEN_WIDTH // 2 - (TEXT_AND_BUTTON_WIDTH - 50) // 2
    y = SCREEN_HEIGHT - TEXT_AND_BUTTON_HEIGHT - 30
    buttons.append(Button(x, y, TEXT_AND_BUTTON_WIDTH - 50, TEXT_AND_BUTTON_HEIGHT, "Registrieren"))

    screen.fill(Colors.BACKGROUND_COLOR)
    headline_surface = headline_font.render(headline_text, True, Colors.HEADLINE_COLOR)
    headline_rect = headline_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
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
                            print("hat geklappt")
            for input in input_fields:
                input.handle_event(event)
        for button in buttons:                    
            button.draw(screen, pygame.mouse.get_pos())

        for input in input_fields:
            input.draw(screen)
        pygame.display.update()