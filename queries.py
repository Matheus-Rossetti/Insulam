import sqlite3

# conn = sqlite3.connect(':memory:') // use RAM for db

def insert_new_user(user_name, email, password):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    # Using parameterized query to insert data safely
    c.execute("""
        INSERT INTO accounts (user_name, email, password)
        VALUES (?, ?, ?)
    """, (user_name, email, password))

    conn.commit()
    conn.close()
