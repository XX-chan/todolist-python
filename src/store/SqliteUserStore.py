import sqlite3
from model.user import User

class SqliteUserStore:
    def __init__(self,db_path="data/users.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            created_at DATE DEFAULT CURRENT_DATE)""")
        self.conn.commit()
        
    def add(self, user):
        self.conn.execute("""
            INSERT INTO users(username, password_hash,created_at)
            VALUES(?,?,?)
        """,(
            user.username,
            user.password_hash,
            user.created_at
            ))
        self.conn.commit()

    def get_by_username(self, username):
        cursor = self.conn.execute("""
            SELECT user_id,username,password_hash,created_at
            FROM users WHERE username=?
        """,(username,))
        row = cursor.fetchone()
        if row:
            return User(*row)
        return None