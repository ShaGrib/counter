from datetime import timedelta
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ggwerr3456xxzaihgebn79'
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/')
def base_load():
    session.permanent = True
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1   
    return render_template('index.html')

@app.route('/count')
def increase_count():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)