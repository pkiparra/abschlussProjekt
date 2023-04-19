import pygame
import pyautogui

from Board import Board

pygame.init()

WINDOWSIZE = (600, 600)
screen = pygame.display.set_mode(WINDOWSIZE)

board = Board(WINDOWSIZE[0], WINDOWSIZE[1])

font = pygame.font.SysFont(None, 24)
img = font.render("hello", True, "blue")


def draw(display):
    display.fill("white")
    pygame.display.set_caption(f"It's {board.turn}'s turn")
    board.draw(display)
    pygame.display.update()


if __name__ == "__main__":
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                pyautogui.alert("Schwarz und Weiß beginnen beide mit sechs Bauern.\nJeder Bauer kann ein oder zwei Felder nach vorne ziehen, Letzteres falls sich dieser Bauer noch nicht zuvor bewegt hatte.\nZugleich kann jeder Bauer auf ein Feld, das sich diagonal vor ihm befindet, ziehen, falls dieses von einem gegnerischen Bauer besetzt ist, damit eliminiert er diesen Bauern.\n\nWenn alle Gegnerischen Bauern eliminiert sind oder ein Bauer die letzte Reihe erreicht, ist das Spiel für den Spieler dieser Farbe gewonnen.\nFalls eine Seite in ihrer Runde keinen Zug spielen kann, kommt es zu einem Unentschieden.", "Regeln des Bauernschachs", "Verstanden!")

            if event.type == pygame.MOUSEBUTTONDOWN and board.turn == "white":
                board.handleClick(event.button, mx, my)
            
            if board.turn == "black":
                if board.getStatus() != "continue":
                    break

                (beta, bestAction) = board.alphaBetaMinimax("black", -1000000, 1000000, 4)
                board.makeMove(bestAction[0], bestAction[1], False)
                board.turn = "white"

        status = board.getStatus()
        if status != "continue":
            if status == "draw":
                print("Draw!")
            else:
                print(f"{status.capitalize()} wins")

            running = False

        draw(screen)
