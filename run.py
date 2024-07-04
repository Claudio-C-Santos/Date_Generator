import os
from flask import Flask
from selector_functions import text as input_text

app = Flask(__name__)

@app.route("/")
def index():
    return input_text


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)