from flask import Flask, render_template, request, redirect

app = Flask(__name__)

complaints = []


@app.route("/")
def home():
    return render_template("index.html", complaints=complaints)


@app.route("/complaint", methods=["POST"])
def add_complaint():
    complaint = {
        "name": request.form["name"],
        "room": request.form["room"],
        "category": request.form["category"],
        "description": request.form["description"]
    }

    complaints.append(complaint)

    return redirect("/")


@app.route("/api/complaints")
def api_complaints():
    return complaints


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)