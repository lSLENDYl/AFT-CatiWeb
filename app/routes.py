from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request
import simplifierscript

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Miguel'}
  return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect('/index')
  return render_template('login.html', title='Sign In', form=form)

@app.route('/editor')
def editor():
    return render_template('editor.html', title='Редактор текста')

@app.route('/simplifier', methods=["GET", "POST"])
def simplifier():
    if request.method == "POST":
        input_text = request.form["input_text"]
        simplified_text = simplifierscript.simplify_text(input_text)
        print(simplified_text)
        return render_template("simplifier.html", title='Упроститель текста', simplified_text=simplified_text, input_text=input_text)
    return render_template("simplifier.html", title='Упроститель текста', simplified_text="", input_text="")

@app.route('/help')
def help():
    return render_template('help.html', title='Помощь')