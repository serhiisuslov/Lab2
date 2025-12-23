from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/content")
def content():

    content_type = request.headers.get("Content-Type")

    if content_type == "application/json":
        return jsonify({"content": "JSON response"})

    elif content_type == "application/xml":
        return """<?xml version="1.0" encoding="UTF-8"?>
        </response>
        <message>XML response</message>
        """

    else:
        return "Plain text message"

if __name__ == '__main__':
    app.run(port=8000)