from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
import os
from pymongo import MongoClient

app = Flask(__name__)

# put your atlas uri here or set MONGO_URI
MONGO_URI = os.environ.get(
    "MONGO_URI",
    "mongodb+srv://USERNAME:PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
)
DB_NAME = "devopsdb"
COLLECTION = "submissions"


def get_collection():
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=8000)
    client.admin.command("ping")
    return client[DB_NAME][COLLECTION]


@app.route("/")
def home():
    error = request.args.get("error")
    return render_template("index.html", error=error)


@app.route("/api")
def api():
    # read list from backend file
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email:
        return render_template(
            "index.html",
            error="Name and email are required.",
            name=name,
            email=email,
            message=message,
        )

    doc = {"name": name, "email": email, "message": message}

    try:
        col = get_collection()
        col.insert_one(doc)
        return redirect(url_for("success"))
    except Exception as e:
        # stay on same page, show error
        return render_template(
            "index.html",
            error=str(e),
            name=name,
            email=email,
            message=message,
        )


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
