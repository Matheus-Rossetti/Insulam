CREATE TABLE IF NOT EXISTS accounts (
    user_id INTEGER PRIMARY KEY,
    user_name TEXT,
    email TEXT,
    password TEXT
);

INSERT INTO accounts VALUES('Matheus', 'Rossetti', 'matheuzdreher@gmail.com', 'Matheus-16') -- test


SELECT user_name FROM accounts
WHERE user_name = "teste";