from data.db_connection import get_connection

class UserInfo:

    @staticmethod
    def create_account(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (username, password)
        VALUES(?, ?)
        ''', (username, password))
        conn.commit()
        conn.close()

    @staticmethod
    def get_user(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, password FROM users WHERE username = ?
        ''', (username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            user_id, stored_password = user
            if stored_password == password:
                return user_id
        return None