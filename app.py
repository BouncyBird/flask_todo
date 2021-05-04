from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta

app = Flask(__name__)

<<<<<<< HEAD
app.config['SECRET_KEY'] = '172f64ded4c61bea7642e3eac02b32cb'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=500)
=======
# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'put secret key here'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
>>>>>>> 39ed2190200197021911ff6c32d116ccd27ce452


@app.route('/')
def home():
    try:
        todo_list = session['tasks']
    except:
        todo_list = []
    return render_template("base.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    try:
        session['tasks'].append({'title': title, 'complete': False})
        session.modified = True
        llen = len(session['tasks']) - 1
        l = session['tasks'][llen]
        l['id'] = llen
    except:
        session['tasks'] = [{'title': title, 'complete': False}]
        session.permanent = True
        llen = len(session['tasks']) - 1
        l = session['tasks'][llen]
        l['id'] = llen
    flash("Task Created!", "success")
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    d = session['tasks'][todo_id]
    d['complete'] = not d['complete']
    flash("Task Updated!", "success")
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    session['tasks'].pop(todo_id)
    flash("Task Deleted!", "danger")
    return redirect(url_for("home"))

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=False)
=======
    db.create_all()
    app.run(debug=True)
>>>>>>> 39ed2190200197021911ff6c32d116ccd27ce452
