import pygame, choose_game_view

from ui_elements.Button import Button
from ui_elements.Button_types import Button_types
from classes import User
# Beispieldaten für das Leaderboard
leaderboard_data = [
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1/2, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 3/1, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
    {"name": "Spieler 4","schwierigkeitsgrad": "leicht", "siege": 1, "niederlagen":0, "tictactoe": 0, "bauernschach": 1},
    {"name": "Spieler 5", "schwierigkeitsgrad": "leicht", "siege": 0, "niederlagen":0, "tictactoe": 0, "bauernschach": 0},
]
 
class LeaderboardGUI:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.surface.fill((230, 230, 230))
 
        font = pygame.font.SysFont('Arial', 20, bold=True)
        self.header_names = ["Spielername", "gamemode", "wins/losses"]
        for i, name in enumerate(self.header_names):
            header_label = font.render(name, True, (42, 157, 143))
            header_label_rect = header_label.get_rect(x=50 + i * 180, y=50)
            self.surface.blit(header_label, header_label_rect)
 
        font = pygame.font.SysFont('Arial', 20)
        for i, data in enumerate(leaderboard_data):
            row = i + 1
            name_label = font.render(data["name"], True,(33, 33, 33))
            name_label_rect = name_label.get_rect(x=80, y=50 + row * 50)
            self.surface.blit(name_label, name_label_rect)
 
            schwierigkeitsgrad_label = font.render(data["schwierigkeitsgrad"], True,(33, 33, 33))
            schwierigkeitsgrad_label_rect = schwierigkeitsgrad_label.get_rect(x=250, y=50 + row * 50)
            self.surface.blit(schwierigkeitsgrad_label, schwierigkeitsgrad_label_rect)
 
            siege_label = font.render(str(data["siege"]), True, (0, 0, 0))
            siege_label_rect = siege_label.get_rect(x=450, y=50 + row * 50)
            self.surface.blit(siege_label, siege_label_rect)
 
pygame.init()

def draw_view(screen: pygame.Surface, user: User): 
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    surface_width, surface_height = 1600, 1200
    surface = pygame.Surface((surface_width, surface_height))
    
    back_button = Button(10, 10, 40, 40, Button_types.BACK)

    pygame.display.set_caption("Leaderboard")
    leaderboard = LeaderboardGUI(surface)
    
    scroll_position = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.was_clicked(event):
                    choose_game_view.draw_view(screen, user)
                elif event.button == 4:  
                    scroll_position += 20
                elif event.button == 5:  
                    scroll_position -= 20


        scroll_position = min(max(scroll_position, 0), surface_height - screen_height)
    
        screen.fill((0, 0, 0, 0))
        screen.blit(surface.subsurface(pygame.Rect(0, scroll_position, screen_width, screen_height)), (0, 0))

        back_button.draw(screen, pygame.mouse.get_pos())
        pygame.display.update()
    
    pygame.quit()