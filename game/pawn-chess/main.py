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
