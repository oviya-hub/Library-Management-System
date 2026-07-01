from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database.database import get_connection

auth = Blueprint("auth", __name__)


@auth.route("/")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_user():

    librarian_id = request.form["librarian_id"]
    password = request.form["password"]

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM librarians
        WHERE librarian_id=%s
        AND password=%s
        """,
        (librarian_id, password)
    )

    librarian = cursor.fetchone()

    cursor.close()
    connection.close()

    if librarian:

        session["librarian"] = librarian["librarian_name"]

        return redirect(url_for("dashboard"))

    flash("Invalid Librarian ID or Password")

    return redirect(url_for("auth.login"))


@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))