from flask import Flask, request
from flask import render_template
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    print(request.headers)
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
