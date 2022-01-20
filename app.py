from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=500)


@app.route('/')
def home():
    try:
        todo_list = session['tasks']
    except KeyError:
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
    except KeyError:
        session['tasks'] = [{'title': title, 'complete': False}]
        session.permanent = True
        l = session['tasks'][0]
        l['id'] = 0
    flash("Task Created!", "success")
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    d = session['tasks'][todo_id]
    d['complete'] = not d['complete']
    flash("Task Updated!", "success")
    lenn = 0
    for i in session['tasks']:
        i['id'] = lenn
        lenn += 1
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    session['tasks'].pop(todo_id)
    flash("Task Deleted!", "danger")
    lenn = 0
    for i in session['tasks']:
        i['id'] = lenn
        lenn += 1
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=False)
