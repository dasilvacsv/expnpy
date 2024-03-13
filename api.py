from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def setup_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS accounts (name TEXT, balance REAL)')
    conn.close()

setup_db()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    accounts = conn.execute('SELECT * FROM accounts').fetchall()
    conn.close()
    return render_template('index.html', accounts=accounts)

@app.route('/add_account', methods=('GET', 'POST'))
def add_account():
    if request.method == 'POST':
        account_name = request.form['account_name']
        initial_balance = request.form['initial_balance']
        conn = get_db_connection()
        conn.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)',
                     (account_name, initial_balance))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_account.html')

if __name__ == '__main__':
    app.run()