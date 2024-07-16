from flask import *

app = Flask(__name__)


@app.route('/')
def main_route():
    return render_template(r'index.html')


if __name__ == "__main__":
    app.run(debug=True)
