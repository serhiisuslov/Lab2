from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/currency")
def hello_world():
    today = request.args.get("today")
    key = request.args.get("key")

    return "USD - 41,5"

if __name__ == '__main__':
    app.run(port=8000)