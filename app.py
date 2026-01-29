from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000), host="0.0.0.0")
