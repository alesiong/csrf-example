from flask import Flask
from flask import make_response, render_template, request, redirect, abort

app = Flask(__name__)

magic = 'a0s030czxoSDJFo90(D'

@app.route('/')
def index():
    return render_template('integrate.html')


@app.route('/cookie')
def set_cookie():
    response = make_response('')
    response.set_cookie('name', magic)
    return response


@app.route('/post', methods=['POST'])
def post_form():
    if request.cookies.get('name') != magic:
        return abort(401)
    print(request.form.get('money'))
    return redirect('/')