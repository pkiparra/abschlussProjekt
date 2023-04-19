import pygame


class Pawn:
    def __init__(self, pos, color, tileSize):
        self.pos = pos
        self.color = color
        self.tileSize = tileSize
        self.hasMoved = False
        self.sprite = self.loadSprite(f"sprites/{color}/pawn.png")
        self.originalSprite = self.sprite.copy()

    def loadSprite(self, path):
        sprite = pygame.image.load(path)
        return pygame.transform.scale(
            sprite, (self.tileSize[0] - 35, self.tileSize[1] - 35)
        )

    def getMoves(self):
        return (
            [(0, -1), (-1, -1), (1, -1), (0, -2)]
            if self.color == "white"
            else [(0, 1), (1, 1), (-1, 1), (0, 2)]
        )

    def setActive(self, active):
        if active:
            self.sprite = self.loadSprite("sprites/piece_selected.png")
        else:
            self.sprite = self.originalSprite
