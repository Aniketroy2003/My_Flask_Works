from flask import Flask,render_template



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route("/<name>")
# def user(name):
#     return f"hello! {name}, So this is the first Page"

@app.route('/render')
def neo():
    return render_template('index.html',content=['Aniket','Vinit','Abhishek'])

if __name__ == "__main__":
    app.run()