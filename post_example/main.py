from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receiving_pass():
    error = None
    if request.method == 'POST':
        return f'<h1>Username: {request.form["name"]}, Password: {request.form["password"]}</h1>'
    return 'Not Good'


if __name__ == '__main__':
    app.run(debug=True)
