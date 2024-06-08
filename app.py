from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return redirect(url_for('login_step', step=1))

@app.route('/login_step/<int:step>', methods=['GET', 'POST'])
def login_step(step):
    if request.method == 'POST':
        if step == 1:
            session['username'] = request.form['username']
        elif step == 2:
            session['password'] = request.form['password']
        return redirect(url_for('login_step', step=step+1))

    return render_template(f'step{step}.html', step=step)

@app.route('/summary')
def summary():
    return render_template('summary.html', username=session.get('username'), password=session.get('password'))

if __name__ == '__main__':
    app.run(debug=True)
