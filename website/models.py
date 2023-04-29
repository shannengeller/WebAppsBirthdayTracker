from flask import Flask, render_template, request, redirect, url_for
import sqlite3




app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('birthdays.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS birthdays
                   (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, relationship TEXT, dob TEXT, gift_ideas TEXT)''')
    conn.commit()
    conn.close()

init_db()


@models.route('/')
def index():
    return render_template('BT-EnterBDay.html')

@models.route('/BT-EnterBDay.html', methods=['POST'])
def enterBDay():
    first_name = request.form['inputFirstName']
    last_name = request.form['inputLastName']
    relationship = request.form['relationship']
    dob = request.form['dob']
    gift_ideas = request.form['giftIdeas']

    conn = sqlite3.connect('birthdays.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO birthdays (first_name, last_name, relationship, dob, gift_ideas) VALUES (?, ?, ?, ?, ?)''', (first_name, last_name, relationship, dob, gift_ideas))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
