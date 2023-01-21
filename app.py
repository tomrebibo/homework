from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route("/")
def home():
    return ' <h1 style="color:red;">  MiSSion Complete tom KIng<h1>'

if __name__ == "__main__" :
    app.run()
