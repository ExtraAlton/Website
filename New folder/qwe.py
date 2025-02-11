from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('qwe.html')

@app.route('/contact')
def contact():
    return render_template('rty.html')

@app.route('/login')
def login():
    return render_template('uio.html')

@app.route('/signup')
def signup():
    return render_template('pas.html')

if __name__ == '__main__':
    app.run(debug=True)