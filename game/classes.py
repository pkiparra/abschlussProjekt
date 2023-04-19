from enum import Enum

class Difficulty(Enum):
    EASY = "leicht"
    MEDIUM = "mittel"
    HARD = "schwer"

class User:

    def __init__(self, username: str = "guest", ):
        self.difficulty: Difficulty = Difficulty.EASY
        self.username = username
    
class Winner(Enum): 
    USER = "user"
    AI = "ai"