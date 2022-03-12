from flask import Flask, render_template, request, url_for, redirect
import random


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    code_list = ["21CE93","AP4RB7","878TRT","AD34S9","A4214S","QR39B8","TX5R23","54WPI4","47SDE4","384ADA","73G8S7","87D8XZ","TQ14E2","1RE15P","M4T33S"]
    verify = random.choice(code_list)
    if request.method == "POST":
        data = request.form
        username = "test"
        password = "test"
        if data["username"] == username and data["password"] == password and data["captcha"] in code_list or data["captcha"] == "":
            return redirect(url_for('success'))
        else:
            return render_template("login.html",value=verify)
    else:
        return render_template("login.html",value=verify)

@app.route("/success")
def success():
    return render_template("success.html")

app.config['SECRET_KEY'] = "Mustafa Öztaş"

if __name__=="__main__":
	app.run(hostname='0.0.0.0')
