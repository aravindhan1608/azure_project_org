from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template("index.html")  
@app.route('/AesculusHippocastanum.html')
def AesculusHippocastanum():
    return render_template("AesculusHippocastanum.html")
@app.route('/BetalLeafPlant.html')
def BetalLeafPlant():
    return render_template("BetalLeafPlant.html")
@app.route('/Eveningprimroseoil.html')
def Eveningprimroseoil():
    return render_template("Eveningprimroseoil.html")
@app.route('/gingko.html')
def gingko():
    return render_template("gingko.html")
@app.route('/Gulvelplant.html')
def Gulvelplant():
    return render_template("Gulvelplant.html")
@app.route('/keezhanelli.html')
def keezhanelli():
    return render_template("keezhanelli.html")
@app.route('/holymangrove.html')
def holymangrove():
    return render_template("holymangrove.html")    
@app.route('/MultivitaminPlant.html')
def MultivitaminPlant():
    return render_template("MultivitaminPlant.html")
@app.route('/RutaGraveolens.html')
def RutaGraveolens():
    return render_template("RutaGraveolens.html")
   
@app.route('/Sambucus.html')
def Sambucus():
    return render_template("Sambucus.html")
@app.route('/Terminalia.html')
def Terminalia():
    return render_template("Terminalia.html")
@app.route('/Rose.html')
def Rose():
    return render_template("Rose.html")
@app.route('/Marigold.html')
def Marigold():
    return render_template("Marigold.html")
@app.route('/Lavanda.html')
def Lavanda():
    return render_template("Lavanda.html")
@app.route('/Jasmine.html')
def Jasmine():
    return render_template("Jasmine.html")
@app.route('/Hibiscus.html')
def Hibiscus():
    return render_template("Hibiscus.html")
@app.route('/herbalplants.html')
def herbalplants():
    return render_template("herbalplants.html")            
@app.route('/flowers.html')
def flowers():
    return render_template("flowers.html")
@app.route('/Echinacea.html')
def Echinacea():
    return render_template("Echinacea.html")
@app.route('/contact.html')
def contact():
    return render_template("contact.html")
@app.route('/checkout.html')
def checkout():
    return render_template("checkout.html")
@app.route('/order.html')
def order():
    return render_template("order.html")
@app.route('/chamomile.html')
def chamomile():
    return render_template("chamomile.html")
@app.route('/Calendula.html')
def Calendula():
    return render_template("Calendula.html") 
@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html") 

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('database.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);""")

        # Check if the username already exists
        cursor.execute("SELECT * FROM users1 WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return 'Username already exists!'
        else:
            # Insert new user into the database
            cursor.execute("INSERT INTO users1 (username, password) VALUES (?, ?)", (username, generate_password_hash(password)))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = connect_db()
        cursor = conn.cursor()

        # Retrieve user from the database
        cursor.execute("SELECT * FROM users1 WHERE username=?", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session['logged_in'] = True
            conn.close()
            return redirect('/')
        else:
            conn.close()
            return 'Incorrect username or password'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
