from urllib import request
from flask import Flask,render_template,request,url_for,redirect,session,flash,get_flashed_messages
from datetime import timedelta



app = Flask(__name__)
app.secret_key = 'Hello'        #-----secret key
app.permanent_session_lifetime = timedelta(seconds=20)   #------session timings

# =========== home page
@app.route("/home")
def home():
    return render_template('home.html')

# ========== about page
@app.route("/about")
def about():
    return render_template('about.html')

# ======== contact page
@app.route("/contact")
def contact():
    return render_template('contact.html')


# ========= login module
@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['name']
        session['user'] = user
        flash("Login is success")
        return redirect(url_for('user'))
        # return redirect(url_for('user',usr=user))
    else:
        if 'user' in session:
            flash("Already logged in ....")
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user')
# def user(usr):
def user():
    if 'user' in session:
        user = session['user']
        print("===============you are logged in=============")
        return render_template('user.html',user=user)
    else:
        flash(f"you are logged in as {user}")
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop("user",None)
    print("logout=============")
    flash("you have been logged out!","info")
    return redirect((url_for("login")))
    




# @app.route("/<name>")
# def user(name):
#     return f"hello! {name}, So this is the first Page"

@app.route('/render')
def neo():
    return render_template('index.html',content=['Aniket','Vinit','Abhishek'])

if __name__ == "__main__":
    app.run(debug=True)