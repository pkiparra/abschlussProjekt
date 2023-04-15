import db

def start_game():
    
    db.setup_db()
    print(db.create_user("julian", "123456789"))
    print(db.is_username_available("Kurt"))
    print(db.get_password_for_user("julian"))
if __name__ == "__main__":
    start_game()