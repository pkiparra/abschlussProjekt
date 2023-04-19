import db
from classes import User, Game
import TicTacToe, choose_game_view

def register_user(user_inputs) -> User:
    username = user_inputs[0]
    password = user_inputs[1]
    confirmed_password = user_inputs[2]

    if username == "" or password == "" or confirmed_password == "":
         raise Exception("Bitte alle Felder ausfüllen")

    if password != confirmed_password: 
        print("passwords dont match")
        raise Exception("Passwörter stimmen nicht überein!")
    elif db.is_username_available(username) and username != "guest":
            db.create_user(username, password)
            return User(username)
    else:
         raise Exception("Username existiert bereits!")
    
def login_user(user_inputs) -> User:
    username = user_inputs[0]
    password = user_inputs[1]

    if username == "" or password == "":
         raise Exception("Bitte alle Felder ausfüllen")
    db_password = db.get_password_for_user(username)
    if db_password:
        if password == db_password: 
            print("passwords for User match")
            return User(username)
        else:
            print("passwords dont match")
            raise Exception("Username oder Passwort Falsch!")
    else:
         raise Exception("Username oder Passwort Falsch!")
    
def play_tic_tac_toe (screen, user: User):
    userWon = TicTacToe.draw_view()
    db.write_game_result_in_db(user.username, Game.TIC_TAC_TOE.value, user.difficulty, userWon)
    choose_game_view.draw_view(screen, user)
