from flask import Flask, request
from flask import render_template
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/mypage/me')
def message():
    return render_template("about_me.html")


@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        print(request.form)
        return redirect("/mypage/contact")


