from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request, jsonify
from app import simplifierscript, editorscript

latest_text = ""

@app.route('/handle-space', methods=['POST'])
def handle_space():
    global latest_text
    data = request.get_json()
    if data.get('text', '').strip() != latest_text.strip():
        latest_text = data.get('text', '')
        editor(latest_text)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'empty'})


@app.route('/process-text', methods=['POST'])
def process_text():
    input_html = request.get_json().get('text', '')
    simplified_html = editorscript.simplify_text(input_html)
    return jsonify({'simplified_text': simplified_html})

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
    # return render_template('editor.html', title='Редактор текста')
    if text:
        print(text)
        simplified_text = editorscript.simplify_text(text)
        # print(simplified_text)
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