import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

complaints = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        complaints=complaints,
        commit_id=os.getenv("COMMIT_ID", "local")
    )


@app.route("/complaint", methods=["POST"])
def add_complaint():
    name = request.form["name"].strip()
    room = request.form["room"].strip()
    category = request.form["category"].strip()
    description = request.form["description"].strip()

    if not name or not room or not category or not description:
        return "All fields are required", 400

    complaint = {
        "name": name,
        "room": room,
        "category": category,
        "description": description
    }

    complaints.append(complaint)

    return redirect("/")


@app.route("/api/complaints")
def api_complaints():
    return complaints


@app.route("/health")
def health():
    return {
        "status": "ok",
        "commit": os.getenv("COMMIT_ID", "local")
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)