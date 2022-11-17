from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<aaa>')
def index(aaa: str):
    return render_template("index.html", aaa=aaa)


if __name__ == '__main__':
    app.run("0.0.0.0", 3000, debug=False)
