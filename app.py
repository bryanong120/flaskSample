from flask import Flask, render_template, request
import requests
from webargs import flaskparser, fields
import re

app = Flask(__name__)


# @app.route('/<aaa>')
# def index(aaa: str):
#     return render_template("index.html", aaa=aaa)

def verifySearch(inputText: str):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if len(inputText) == 0:
        print("no input")
        return False

    if(regex.search(inputText) == None):
        print("No illegeal characters")
        return 'TRUE'
    else:
        print("illegal characters in username.")
        return 'FALSE'

@app.route('/', methods =['GET','POST'])
def main():
    if request.method == 'POST':
        text_id = request.form['searchtxt']

        if (verifySearch(text_id)) == 'TRUE':
            return render_template("sucessPage.html", searchtxt = text_id)
        else:
            return render_template("home.html")
    return render_template("home.html")

@app.route('/backHome', methods =['GET','POST'])
def backHome():
    if request.method == "POST":
        return render_template("home.html")



if __name__ == '__main__':
    app.run("0.0.0.0", 3000, debug=False)
