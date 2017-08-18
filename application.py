from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
        
@app.route("/city")
def city():
    return render_template("city.html")
        
@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")
    
@app.route("/dish")
def dish():
    return render_template(".html")    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    