from flask import Blueprint, render_template, request, redirect, url_for
from database.database import get_connection

books = Blueprint("books", __name__)


# ----------------------------
# View Books
# ----------------------------
@books.route("/books")
def manage_books():

    search = request.args.get("search", "")

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    if search:

        cursor.execute("""
            SELECT *
            FROM books
            WHERE accession_no LIKE %s
               OR title LIKE %s
               OR author LIKE %s
               OR category LIKE %s
            ORDER BY title
        """, (
            "%" + search + "%",
            "%" + search + "%",
            "%" + search + "%",
            "%" + search + "%"
        ))

    else:

        cursor.execute("""
            SELECT *
            FROM books
            ORDER BY title
        """)

    all_books = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "books.html",
        books=all_books,
        search=search
    )


# ----------------------------
# Save Book
# ----------------------------
@books.route("/save_book", methods=["POST"])
def save_book():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO books
        (
            accession_no,
            title,
            author,
            category,
            publisher,
            year_published,
            isbn,
            copies
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (

        request.form["accession_no"],
        request.form["title"],
        request.form["author"],
        request.form["category"],
        request.form["publisher"],
        request.form["year_published"],
        request.form["isbn"],
        request.form["copies"]

    ))

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("books.manage_books"))


# ----------------------------
# Delete Book
# ----------------------------
@books.route("/delete_book/<int:id>")
def delete_book(id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id=%s",
        (id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("books.manage_books"))