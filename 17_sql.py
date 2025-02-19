import sqlite3

conn = sqlite3.connect('company_db.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
              id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              age INTEGER NOT NULL,
              salary REAL NOT NULL
              )
              ''')
c.execute("INSERT INTO employees (id,name, age, salary) VALUES (1,'Aakash', 20, 50000)")
c.execute("INSERT INTO employees (id,name, age, salary) VALUES (2,'Kowshik', 21, 55000)")
c.execute("INSERT INTO employees (id,name, age, salary) VALUES (3,'Abi', 22, 30000)")
c.execute("INSERT INTO employees (id,name, age, salary) VALUES (4,'John Doe', 21, 45000)")

c.execute("SELECT * FROM employees WHERE salary > 40000")

rows = c.fetchall()
print(rows)