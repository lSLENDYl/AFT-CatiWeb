from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

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

@app.route('/simplifier')
def simplifier():
    return render_template('simplifier.html', title='Упроститель текста')

@app.route('/help')
def help():
    return render_template('help.html', title='Помощь')