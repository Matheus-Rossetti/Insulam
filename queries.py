import sqlite3


# conn = sqlite3.connect(':memory:') // use RAM for db

def insert_new_user(user_name, email, password):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    c.execute("""
        INSERT INTO accounts (user_name, email, password)
        VALUES (?, ?, ?)
    """, (user_name, email, password))

    conn.commit()
    conn.close()


def select_password_from_user(user_name):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    # Utilize um parâmetro posicional para evitar SQL Injection
    c.execute("""SELECT password FROM accounts WHERE user_name = ?""",
              (user_name,))

    result = c.fetchone()
    print(result)
    conn.close()

    return result[0]

def select_user(user_name):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    c.execute(""" SELECT user_name FROM accounts
                        WHERE user_name = (?);""",
              (user_name,))

    result = c.fetchone()
    conn.close()

    return result

if __name__ == '__main__':
    pass