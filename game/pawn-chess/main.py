import pygame

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.handleClick(event.button, mx, my)

        status = board.getStatus()
        if status != "continue":
            if status == "draw":
                print("Draw!")
            else:
                print(f"{status.capitalize()} wins")

            running = False

        draw(screen)
