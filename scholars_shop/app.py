from flask import Flask, render_template

app = Flask(__name__)
   
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/register')
def register_page():
    return render_template ('register.html') 

@app.route('/login')
def login_page():
    return render_template ('login.html') 

@app.route('/market')
def market():
    return render_template('market.html')

if __name__ == '__main__':
    app.run(debug=True)