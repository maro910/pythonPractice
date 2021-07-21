from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/") #if the user is on domain, run home function
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form['variable']
        return redirect(url_for("user", usr=user))
    return render_template("login.html")

@app.route("/<usr>", methods=["POST"])
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    
    
    
    
    
    
    
    
    
"""
# if user types in random url, run user function
@app.route("/<name>") #what user puts in url will be passed as param in def user
def user(name):
    return f"Hello {name}"

@app.route("/hey")
# redirect to home page
def hey():
    return redirect(url_for("user", name="Admin!")) #pass in def in string

"""