from flask import *
from queries import *
import hashlib
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template(r'login.html')
    elif request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        password = hashlib.sha256(password.encode()).hexdigest()

        real_password = select_password_from_user(user_name)

        if password == real_password:
            return redirect(url_for('show_user_profile', user_name=user_name))
        else:
            return "Incorrect Password"


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template(r'create_user.html')
    elif request.method == 'POST':
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = select_user(user_name)

        if user_name in existing_user:
            return "User already exists"

        password = hashlib.sha256(password.encode()).hexdigest()

        insert_new_user(user_name, email, password)

        return redirect('/login')


@app.route('/user/<user_name>')
def show_user_profile(user_name):
        return f'{user_name}\'s profile'

if __name__ == "__main__":
    app.run(debug=True)
