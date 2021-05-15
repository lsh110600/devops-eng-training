from flask import Flask, render_template
from functions import add, sub, div, mul
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기

@app.route("/add")
def app_add():
    n1, n2 = request.args.get('n1'), request.args.get('n2')
    return add(n1, n2)

@app.route("/sub")
def app_sub():
    n1, n2 = request.args.get('n1'), request.args.get('n2')
    return sub(n1, n2)


@app.route("/div")
def app_div():
    n1, n2 = request.args.get('n1'), request.args.get('n2')
    return div(n1, n2)


@app.route("/mul")
def app_mul():
    n1, n2 = request.args.get('n1'), request.args.get('n2')
    return mul(n1, n2)


def create_app():
    return app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
