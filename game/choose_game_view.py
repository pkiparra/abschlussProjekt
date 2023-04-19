import pygame, start_app_view, app_backend
from ui_elements.Colors import Colors
from ui_elements.Button import Button
from ui_elements.Stay_clicked_button import Stay_clicked_button
from ui_elements.Error import Error
from ui_elements.Button_types import Button_types
from classes import User, Difficulty
pygame.init()

TEXT_AND_BUTTON_WIDTH = 200
TEXT_AND_BUTTON_HEIGHT = 50
TEXT_AND_BUTTON_SPACING = 50

headline_font = pygame.font.SysFont(None, 64)
choose_difficulty_font = pygame.font.SysFont(None, 25)
headline_text = "Ai mini games"
choose_difficulty_text = "Gamemode wählen:"
text_input_titles = ["username", "Passwort"]

def draw_view(screen, user: User):
    print(f'{user.username} logged in')

    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()

    buttons = []
    buttons.append(Button(10, 10, 70, 40, Button_types.LOGOUT, 25))
    buttons.append(Stay_clicked_button(150, 115, 95, 40, Button_types.GAMEMODE_EASY, 25))
    buttons.append(Stay_clicked_button(SCREEN_WIDTH / 2 - 95 / 2, 115, 95, 40, Button_types.GAMEMODE_MEDIUM, 25))
    buttons.append(Stay_clicked_button(SCREEN_WIDTH - 150 - 95, 115, 95, 40, Button_types.GAMEMODE_HARD, 25))
    buttons.append(Button(SCREEN_WIDTH * 0.25 - TEXT_AND_BUTTON_WIDTH / 2, 300, TEXT_AND_BUTTON_WIDTH, TEXT_AND_BUTTON_HEIGHT, Button_types.START_PAWN_CHESS))
    buttons.append(Button(SCREEN_WIDTH * 0.25 - TEXT_AND_BUTTON_WIDTH / 2, 375, TEXT_AND_BUTTON_WIDTH, TEXT_AND_BUTTON_HEIGHT, Button_types.LEADERBOARD_PAWN_CHESS))
    buttons.append(Button(SCREEN_WIDTH * 0.75 - TEXT_AND_BUTTON_WIDTH / 2, 300, TEXT_AND_BUTTON_WIDTH, TEXT_AND_BUTTON_HEIGHT, Button_types.START_TIC_TAC_TOE))
    buttons.append(Button(SCREEN_WIDTH * 0.75 - TEXT_AND_BUTTON_WIDTH / 2, 375, TEXT_AND_BUTTON_WIDTH, TEXT_AND_BUTTON_HEIGHT, Button_types.LEADERBOARD_TIC_TAC_TOE))

    screen.fill(Colors.BACKGROUND_COLOR)
    headline_surface = headline_font.render(headline_text, True, Colors.HEADLINE_COLOR)
    headline_rect = headline_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(headline_surface, headline_rect)
    
    choose_difficulty_surface = choose_difficulty_font.render(choose_difficulty_text, True, Colors.HEADLINE_COLOR)
    choose_difficulty_rect = headline_surface.get_rect(center=(SCREEN_WIDTH // 2, 115))
    screen.blit(choose_difficulty_surface, choose_difficulty_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:        
                for button in buttons:
                    if button.was_clicked(event):
                        if button.title == Button_types.LOGOUT:
                            start_app_view.start_app()
                        if button.title == Button_types.GAMEMODE_EASY:
                            user.difficulty = Difficulty.EASY
                        if button.title == Button_types.GAMEMODE_MEDIUM:
                            user.difficulty = Difficulty.MEDIUM
                        if button.title == Button_types.GAMEMODE_HARD:
                            user.difficulty = Difficulty.HARD
        for button in buttons: 
            if isinstance(button, Stay_clicked_button):
                button.draw(screen, pygame.mouse.get_pos(), user.difficulty.value)   
            else:                
                button.draw(screen, pygame.mouse.get_pos())

        pygame.display.update()