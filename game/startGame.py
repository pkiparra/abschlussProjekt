import db,start_app_view

def start_game():
    
    db.setup_db()
    start_app_view.start_app()
    
if __name__ == "__main__":
    start_game()