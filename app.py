from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")


    # if username == "admin" and password == "123":
    #     return redirect(url_for("welcome"))
    # else:
    #     return redirect(url_for("login"))

    valid_users ={
        'admin':'123',
        'sanju':'1234',
        'sam':'12345'}
    
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html")
    else:
        return "Invalid Usercredentials"
    
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)
