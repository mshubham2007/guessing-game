from flask import Flask, render_template, request, redirect, url_for, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def generate_number_to_guess():
    return random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'number_to_guess' not in session:
        session['number_to_guess'] = generate_number_to_guess()
        session['clicks'] = 0

    if request.method == 'POST':
        if 'reset' in request.form:
            session.pop('number_to_guess')
            session.pop('clicks')
            return redirect(url_for('home'))

        guess = request.form.get('guess')
        if guess is None or not guess.isdigit():
            return render_template('guess.html', message='Invalid input! Guess a number between 1 and 100.', clicks=session['clicks'])

        guess = int(guess)
        session['clicks'] += 1

        if guess == session['number_to_guess']:
            return render_template('win.html', clicks=session['clicks'])
        elif guess < session['number_to_guess']:
            return render_template('guess.html', message='Too low! Guess again.', clicks=session['clicks'])
        else:
            return render_template('guess.html', message='Too high! Guess again.', clicks=session['clicks'])
    
    return render_template('guess.html', message='Guess a number between 1 and 100.', clicks=session['clicks'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
