from enum import Enum

class Button_types(Enum):
    BACK = "<"
    LOGIN = "Login"
    LOGOUT = "logout"
    SIGNUP = "Registrieren"
    PLAY_AS_GUEST = "Als Gast spielen"
    START_PAWN_CHESS = "Spiel startem"
    START_TIC_TAC_TOE = "Spiel startem"
    LEADERBOARD_PAWN_CHESS = "Leaderboard"
    LEADERBOARD_TIC_TAC_TOE = "Leaderboard"
    GAMEMODE_EASY = "leicht"
    GAMEMODE_MEDIUM = "mittel"
    GAMEMODE_HARD = "schwer"
