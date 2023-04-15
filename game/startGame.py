import db

def start_game():
    
    #db.setup_db()
    #print(db.create_user("heinz", "123456789"))
    #print(db.is_username_available("Kurt"))
    #print(db.get_password_for_user("julian"))
    #print(db.user_played_game_before("heinz", "schach", 1))
    db.write_game_result_in_db("hubert", "schach", 2, False)
if __name__ == "__main__":
    start_game()