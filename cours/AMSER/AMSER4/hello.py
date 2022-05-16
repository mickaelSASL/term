from flask import Flask  # pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "sdfsdfsd"

if __name__ == "__main__":
    app.run()