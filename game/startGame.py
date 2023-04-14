import db

def start_game():
    
    db.setup_db()
    print(db.create_user("peter", "passwort"))

if __name__ == "__main__":
    start_game()