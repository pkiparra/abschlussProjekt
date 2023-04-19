import pygame

class Quad:
    def __init__(self, x, y, width, height):
        self.pos = (x, y)
        color = "light" if (x + y) % 2 == 0 else "dark"
        self.drawColor = (200, 200, 200) if color == "light" else (50, 50, 50)
        self.highlightColor = (100, 200, 100) if color == "light" else (10, 200, 10)
        self.occupyingPiece = None
        self.highlight = False
        self.rect = pygame.Rect(x * width, y * width, width, height)

    def getCoord(self):
        columns = "abcdefgh"
        return columns[self.pos[0]] + str(self.pos[1] + 1)

    def draw(self, display):
        if self.highlight:
            pygame.draw.rect(display, self.highlightColor, self.rect)
        else:
            pygame.draw.rect(display, self.drawColor, self.rect)

        if self.occupyingPiece != None:
            centeringRect = self.occupyingPiece.sprite.get_rect()
            centeringRect.center = self.rect.center
            display.blit(self.occupyingPiece.sprite, centeringRect.topleft)
