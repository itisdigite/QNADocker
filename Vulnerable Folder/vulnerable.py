# signup.py (INTENTIONALLY VULNERABLE)
import sqlite3

def signup(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()
    print(f"User {username} added.")

if __name__ == "__main__":
    signup('admin', 'admin123')
