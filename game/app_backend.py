import db

def register_user(user_inputs):
    print("func called")
    username = user_inputs[0]
    password = user_inputs[1]
    confirmed_password = user_inputs[2]

    if username == "" or password == "" or confirmed_password == "":
         raise Exception("Bitte alle Felder ausfüllen")

    if password != confirmed_password: 
        print("passwords dont match")
        raise Exception("Passwörter stimmen nicht überein!")
    elif db.is_username_available(username):
            db.create_user(username, password)
    else:
         raise Exception("Username existiert bereits!")
    
def login_user(user_inputs):
    username = user_inputs[0]
    password = user_inputs[1]

    if username == "" or password == "":
         raise Exception("Bitte alle Felder ausfüllen")
    db_password = db.get_password_for_user(username)
    print(db_password)
    if db_password:
        print("password ist none")
        if password != db_password: 
            print("passwords dont match")
            raise Exception("Username oder Passwort Falsch!")
        else:
             print("passwords for User match")
    else:
         raise Exception("Username oder Passwort Falsch!")