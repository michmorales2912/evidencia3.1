from flask import Flask, render_template, request,redirect, session
import os


app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)

#Index
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
