from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import time

app = Flask(__name__)

app.secret_key = 'c2c954c50e3c5fcdb726d9a7b1b5be0a'  

DATABASE = 'your_database.db'  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username:
            session['username'] = username  
            return redirect(url_for('home'))  
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect(url_for('login')) 

    username = session['username'] 
    if request.method == 'POST':
        answer = request.form['answer']
        timestamp = time.time()  

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''
            INSERT INTO answers (username, timestamp)
            VALUES (?, ?)
        ''', (username, timestamp))
        conn.commit()
        conn.close()

        return redirect(url_for('result', username=username, answer=answer, timestamp=timestamp))

    return render_template('index.html', username=username)

@app.route('/result')
def result():
    username = request.args.get('username')
    answer = request.args.get('answer')
    timestamp = request.args.get('timestamp')
    return render_template('done.html', username=username, answer=answer, timestamp=timestamp)

@app.route('/logout')
def logout():
    session.pop('username', None) 
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
