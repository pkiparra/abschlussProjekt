import db

def start_game():
    
    db.setup_db()
    print(db.create_user("klaus", "passwort"))
    print(db.is_username_available("klaus"))
if __name__ == "__main__":
    start_game()