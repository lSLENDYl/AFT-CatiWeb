from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request, jsonify
from app import simplifierscript, editorscript
from collections import deque

text_versions = deque(maxlen=10)
current_version = 0

@app.route('/handle-space', methods=['POST'])
def handle_space():
    global current_version
    data = request.get_json()
    text_versions.append((current_version, data.get('text', '')))
    current_version += 1
    return jsonify({'status': 'success', 'version': current_version})


@app.route('/process-text', methods=['POST'])
def process_text():
    data = request.get_json()
    input_html = data.get('text', '')

    simplified_html, pairs = editorscript.simplify_text(input_html)

    return jsonify({
        'simplified_text': simplified_html,
        'replacements': pairs,
        'version': current_version
    })

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

@app.route('/editor', methods=["GET", "POST"])
def editor(text=None):
    if text:
        print(text)
        simplified_text = editorscript.simplify_text(text)
        return render_template("editor.html", title='Редактор текста', simplified_text=simplified_text, input_text=text)
    return render_template("editor.html", title='Редактор текста', simplified_text="", input_text="")

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