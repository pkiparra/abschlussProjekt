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