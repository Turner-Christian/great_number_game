from flask import Flask,render_template,request,redirect,session
import random
app = Flask(__name__)
app.secret_key = 'root'

@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,100)
    if 'attempts' not in session:
        session['attempts'] = 0
    else:
        session['attempts'] += 1
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)