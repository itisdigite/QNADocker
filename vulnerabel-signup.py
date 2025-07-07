import sqlite3

# Create a simple database to store users
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
''')
conn.commit()

# Insecure signup function
def signup():
    print("=== Signup Form ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # 🚩 NO INPUT VALIDATION
    # 🚩 STORES PASSWORDS IN PLAIN TEXT
    # 🚩 VULNERABLE TO SQL INJECTION
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(query)
    conn.commit()

    print("User signed up successfully!")

if __name__ == "__main__":
    signup()
