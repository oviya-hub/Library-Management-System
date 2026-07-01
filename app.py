from flask import Flask, render_template, session, redirect, url_for

# Import Blueprints
from modules.auth import auth

app = Flask(__name__)

# Secret key for login sessions
app.secret_key = "library_management_secret_key"

# Register Blueprints
app.register_blueprint(auth)


# ----------------------------
# Dashboard
# ----------------------------
@app.route("/dashboard")
def dashboard():

    if "librarian" not in session:
        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        librarian=session["librarian"]
    )


# ----------------------------
# Run Application
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)