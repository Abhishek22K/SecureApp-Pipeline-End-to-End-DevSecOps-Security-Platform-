import os
import sqlite3
import datetime
from functools import wraps

from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    session,
    g,
    make_response,
)

from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import jwt

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "super-secret-key")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")

DATABASE = os.path.join(app.root_path, "database.db")


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# JWT decorator (kept for demonstration)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("x-access-token")

        if not token:
            return make_response("Token is missing!", 401)

        try:
            data = jwt.decode(
                token,
                app.config["JWT_SECRET_KEY"],
                algorithms=["HS256"]
            )
            current_user = data["username"]
        except Exception:
            return make_response("Token is invalid!", 401)

        return f(current_user, *args, **kwargs)

    return decorated


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        try:
            hashed_password = generate_password_hash(
                password,
                method="scrypt"
            )

            cursor.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (username, hashed_password),
            )

            db.commit()

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:

            return render_template(
                "register.html",
                error="Username already exists."
            )

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,),
        )

        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):

            session["logged_in"] = True
            session["username"] = user["username"]
            session["is_admin"] = user["is_admin"]

            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Invalid credentials"
        )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"],
        is_admin=session["is_admin"],
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))


@app.route("/blog")
def blog():

    db = get_db()

    cursor = db.cursor()

    cursor.execute("""
SELECT
    p.title,
    p.content,
    p.created_at,
    u.username
FROM posts p
JOIN users u ON p.author_id = u.id
ORDER BY p.created_at DESC
""")

    posts = cursor.fetchall()

    return render_template("blog.html", posts=posts)


@app.route("/add_post", methods=["GET", "POST"])
def add_post():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
    "INSERT INTO posts (title, content, author_id) VALUES (?, ?, (SELECT id FROM users WHERE username=?))",
    (title, content, session["username"])
)

        db.commit()

        return redirect(url_for("blog"))

    return render_template("add_post.html")


@app.route("/todo")
def todo():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT id,task,completed
        FROM todos
        WHERE user_id=(
            SELECT id
            FROM users
            WHERE username=?
        )
        """,
        (session["username"],),
    )

    todos = cursor.fetchall()

    return render_template(
        "todo.html",
        todos=todos,
    )


@app.route("/add_todo", methods=["POST"])
def add_todo():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    task = request.form["task"]

    db = get_db()

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO todos(task,user_id)
        VALUES(
            ?,
            (SELECT id FROM users WHERE username=?)
        )
        """,
        (task, session["username"]),
    )

    db.commit()

    return redirect(url_for("todo"))


@app.route("/complete_todo/<int:todo_id>")
def complete_todo(todo_id):

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    db = get_db()

    cursor = db.cursor()

    cursor.execute(
        "UPDATE todos SET completed=1 WHERE id=?",
        (todo_id,),
    )

    db.commit()

    return redirect(url_for("todo"))


@app.route("/admin")
def admin_panel():

    if not session.get("logged_in") or not session.get("is_admin"):
        return redirect(url_for("login"))

    db = get_db()

    cursor = db.cursor()

    search = request.args.get("search", "")

    if search:

        users = cursor.execute(
            f"SELECT id,username,is_admin FROM users WHERE username LIKE '%{search}%'"
        ).fetchall()

    else:

        users = cursor.execute(
            "SELECT id,username,is_admin FROM users"
        ).fetchall()

    return render_template(
        "admin.html",
        users=users,
    )


@app.route("/admin/delete_user/<int:user_id>")
def delete_user(user_id):

    if not session.get("logged_in") or not session.get("is_admin"):
        return redirect(url_for("login"))

    db = get_db()

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,),
    )

    db.commit()

    return redirect(url_for("admin_panel"))


@app.route("/upload", methods=["GET", "POST"])
def upload_file():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":

        if "file" not in request.files:
            return render_template(
                "upload.html",
                error="No file selected"
            )

        file = request.files["file"]

        if file.filename == "":
            return render_template(
                "upload.html",
                error="No filename"
            )

        upload_dir = os.path.join(
            app.root_path,
            "static",
            "uploads"
        )

        os.makedirs(upload_dir, exist_ok=True)

        file.save(
            os.path.join(upload_dir, file.filename)
        )

        return render_template(
            "upload.html",
            message="File uploaded successfully!"
        )

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
