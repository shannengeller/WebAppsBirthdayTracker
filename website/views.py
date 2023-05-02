from flask import Blueprint, render_template, request, Flask
import sqlite3

views = Blueprint('views', __name__)

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('birthdays.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS birthdays
                   (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, relationship TEXT, dob TEXT, gift_ideas TEXT)''')
    conn.commit()
    conn.close()

init_db()

@views.route('/')
def home():
    return render_template("BT-Intro.html")

@views.route('/BT-Intro.html')
def intro():
    return render_template("BT-Intro.html")

@views.route('/BT-EnterBDay.html')
def enterBDay():
    return render_template("BT-EnterBDay.html")

@views.route('/BT-EnterBDay.html', methods=['POST'])
def enterBDay2():
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
    return render_template("BT-EnterBDay.html")

@views.route('/BT-SignIn.html')
def signIn():
    return render_template("BT-SignIn.html")

@views.route('/BT-ViewBDay.html')
def viewBDay():
    conn = sqlite3.connect('birthdays.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM birthdays''')
    data = cur.fetchall()
    conn.close()

    return render_template('BT-ViewBDay.html', data=data)

@views.route('/BT-CreateAccount.html')
def createaccount():
    return render_template("BT-CreateAccount.html")
