from flask import Flask, render_template, url_for, request, make_response, redirect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('register')))
        response.set_cookie('user_name', name)
        response.set_cookie('user_email', email)

        return response

    return render_template('index.html')


@app.route('/register/')
def register():
    user_name = request.cookies.get('user_name')
    user_email = request.cookies.get('user_email')

    return render_template('register.html', user_name=user_name, user_email=user_email)
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')

    return response


if __name__ == '__main__':
    app.run(debug=True)