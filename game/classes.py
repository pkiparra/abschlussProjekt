from enum import Enum

class Difficulty(Enum):
    EASY = "leicht"
    MEDIUM = "mittel"
    HARD = "schwer"

class User:

    def __init__(self, username: str = "guest", ):
        self.difficulty: Difficulty = Difficulty.EASY
        self.username = username
    
class Game(Enum):
    TIC_TAC_TOE = "Tic Tac Toe"
    PAWN_CHESS = "Bauernschach"