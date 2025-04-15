from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])


def register():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")

        if username:
            message = "Registration Successful"
        else:
            message = "Unsuccess"
    
    return render_template("register.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)