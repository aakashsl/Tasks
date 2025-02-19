from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    con = sqlite3.connect('company_database.db')
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                salary REAL NOT NULL
                )
                ''')
    con.commit()
    con.close()
    
init_db()

@app.route('/')
def hello():
    con = sqlite3.connect('company_database.db')
    c=con.cursor()
    c.execute("SELECT * FROM employees")
    rows=c.fetchall()
    con.close()
    return render_template("25.html", rows=rows)

@app.route('/insert',methods=['post'])
def insert():
    con = sqlite3.connect('company_database.db')
    c=con.cursor()
    ids=int(request.form['ids'])
    name=request.form['name']
    age=int(request.form['age'])
    salary=int(request.form['salary'])
    c.execute(f"INSERT INTO employees (id,name, age, salary) VALUES ({ids},'{name}', {age}, {salary})")
    ro=c.fetchall()
    con.commit()
    con.close()
    return redirect(url_for('hello'))

# Update User
@app.route('/update/<int:ids>', methods=['POST'])
def update_user(ids):
    name=request.form['name']
    age=int(request.form['age'])
    salary=float(request.form['salary'])
    con = sqlite3.connect("company_database.db")
    c= con.cursor()
    c.execute(f"UPDATE employees SET name='{name}', age={age}, salary={salary} WHERE id={ids}")
    con.commit()
    con.close()
    return redirect(url_for('hello'))

@app.route('/delete/<int:ids>')
def delete_user(ids):
    con = sqlite3.connect("company_database.db")
    c= con.cursor()
    c.execute(f"DELETE FROM employees WHERE id={ids}")
    con.commit()
    con.close()
    return redirect(url_for('hello'))
    
if __name__ == '__main__':
    app.run(debug=True)