from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events")
def Events():
    return render_template("Events.html")

@app.route("/events")
def delete():
    return render_template("Events.html")

@app.route("/events")
def update():
    return render_template("Events.html")

if __name__ == "__main__":
    app.run(debug= True)