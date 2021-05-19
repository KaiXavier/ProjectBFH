from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy, model

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///eventportal.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class addevent(db.Model):
    sno = db.Column(db.Integer, primary_key= True)
    eventName = db.Column(db.String(200), nullable= False)
    date = db.Column(db.Integer, nullable= False)
    desc = db.Column(db.String(500), nullable= False)
    date = db.Column(db.Integer, nullable= False)
    time = db.Column(db.Integer, nullable= False)
    place = db.Column(db.String(200), nullable= False)
    max_member = db.Column(db.Integer, nullable= False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.eventName} - {self.date} - {self.time}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    # newEvent = addevent()
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)