import sqlite3
import os

def get_connection():
    db_folder = os.path.join("data")
    db_name = "database.db"
    db_path = os.path.join(db_folder, db_name)
    
    return sqlite3.connect(db_path)