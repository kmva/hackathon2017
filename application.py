from flask import Flask, flash, redirect, render_template, request, session, url_for, escape
from models import db, User
from forms import SignUpForm, LoginForm
from flask_session import Session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathon.db'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods = ['GET', 'POST'])
def signup():

    if 'phonenumber' in session:
        return redirect(url_for('city'))
    form = SignUpForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template("signup.html", form=form)
        else:
            newuser = User(form.first_name.data, form.email.data, form.password.data, form.phone_number.data)
            db.session.add(newuser)
            db.session.commit()

            session['phonenumber'] = newuser.phonenumber
            return redirect(url_for('city'))
    elif request.method == 'GET':
        return render_template("signup.html", form=form)

@app.route("/signin", methods = ['GET', 'POST'])
def signin():

    if 'phonenumber' not in session:
        return redirect(url_for('city'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email, first())
            if user is not None and user.check_password(password):
                session["phonenumber"]
                return redirect(url_for('city'))
            else:
                return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('phonenumber', None)
    return redirect(url_for('index'))

@app.route("/city")
def city():
    return render_template("city.html")
    if 'phonenumber' not in session:
        return redirect(url_for('login'))

@app.route("/cofetun")
def restaurants():
    return render_template("cofetun.html")

@app.route("/palazzo")
def dish():
    return render_template("palazzo.html")

@app.route("/mcdowels")
def mcdowels():
    return render_template("cofetun.html")

if __name__ == "__main__":
    app.run(debug=True)

