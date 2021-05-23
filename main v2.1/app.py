from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date, time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///eventDate.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class addevent(db.Model):
    sno = db.Column(db.Integer, primary_key= True)
    eventName = db.Column(db.String(200), nullable= False)
    desc = db.Column(db.String(500), nullable= False)
    date = db.Column(db.Integer, nullable= False)
    time = db.Column(db.Integer, nullable= False)
    place = db.Column(db.String(200), nullable= False)
    max_member = db.Column(db.Integer, nullable= False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.eventName} - {self.date} - {self.time}"


@app.route("/")
def home():
    allEvents = addevent.query.all()
    return render_template("index.html", allEvents=allEvents)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/events", methods = ['GET', 'POST'])
def Events():
    if request.method == 'POST':
        eventName = request.form['eventName']
        date = request.form['date']
        time = request.form['time']
        max_member = request.form['max_member']
        desc = request.form['desc']
        place = request.form['place']

        newEvent = addevent(eventName =eventName, date = date, time = time, max_member = max_member, desc = desc, place = place)
        db.session.add(newEvent)
        db.session.commit()

    allEvents = addevent.query.all()
    return render_template('Events.html', allEvents = allEvents)

@app.route("/delete/<int:sno>")
def delete(sno):
    allEvents = addevent.query.filter_by(sno=sno).first()
    db.session.delete(allEvents)
    db.session.commit()
    return redirect('/events')

@app.route("/events")
def update():
    return render_template("Events.html")

if __name__ == "__main__":
    app.run(debug= True)