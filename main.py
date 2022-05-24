from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"
@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, {name.title()}</p>"

if __name__=='__main__':
    app.run(debug=True)