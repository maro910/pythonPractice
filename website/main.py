from flask import Flask, render_template

# tell flask to use this app name
app = Flask(__name__) # gets the name of the file as the app name


# tell flask what url to serve up

#the main directory
@app.route("/")

def hello_world():
  return "<p>Hello SEOTech developer</p>"

@app.route("/about")

def about():
  return render_template('about.html', subtitle='About Page')

@app.route("/home")

def home():
  return render_template('home.html', subtitle='Home Page')



#terminal command: export FLASK_APP=main
#terminal command: flask run --host=0.0.0.0 how to run environment

#bypass manual environment variable setting and server start

if __name__ == '__main__':
  app.run(host="0.0.0.0")



