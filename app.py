from flask import *
from queries import *

app = Flask(__name__)


@app.route('/')
def main_route():
    return render_template(r'index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template(r'login.html')


@app.route('/select_user')
def select_user():
    pass


@app.route('/create_user', methods=['GET'])
def create_user():
    return render_template(r'create_user.html')


@app.route('/insert_new_user', methods=['POST'])
def create_new_user_route():
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')

    insert_new_user(user_name, email, password)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
