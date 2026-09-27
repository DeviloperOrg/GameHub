import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "gamehub.db"

class Database:
    def __init__(self):
        DATA_DIR.mkdir(exist_ok=True)
        
        self.connection = sqlite3.connect(
            DATABASE_PATH
        )
        
        self.connection.row_factory = sqlite3.Row
        
        self.create_tables()
    
    def create_tables(self):
        cursor = self.connection.cursor()    
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                genre TEXT,
                executable_path TEXT,
                cover_path TEXT,
                favorite INTEGER DEFAULT 0,
                last_played TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )           
            """
        )
        
        self.connection.commit()
        
        
    def add_game(
        self,
        name,
        genre,
        executable_path,
        cover_path,
    ):
        cursor = self.connection.cursor()
        
        cursor.execute("""
           INSERT INTO games(
               name,
               genre,
               executable_path,
               cover_path 
               )
           VALUES (?, ?, ?, ?) 
           """,(name, genre, executable_path, cover_path)
        )
        
        self.connection.commit()
        
        return cursor.lastrowid
    
    def get_games(self):
        
        cursor = self.connection.cursor()
        
        cursor.execute("""
                       SELECT *
                       FROM games
                       ORDER BY name COLLATE NOCASE ASC
                       """)
        return cursor.fetchall()
    
    def delete_game(self, game_id):
        
        cursor = self.connection.cursor()
        
        cursor.execute("""
                       DELETE FROM games
                       WHERE id = ?
                       """,(game_id,))
        
        self.connection.commit()
        
    def close(self)    :
        self.connection.close()
        