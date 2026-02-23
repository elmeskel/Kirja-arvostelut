import sqlite3
import secrets
import re
from flask import Flask
from flask import abort, flash, redirect, render_template, request, session
import config
import markupsafe
import math
import items
import users


app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    page_size = 10
    item_count = items.item_count()
    page_count = math.ceil(item_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))
    all_items = items.get_items(page, page_size)
    return render_template("index.html", items=all_items, page=page, page_count=page_count)

@app.route("/user/<int:user_id>")
@app.route("/user/<int:user_id>/<int:page>")
def show_user(user_id,page=1):
    user = users.get_user(user_id)
    if not user:
        abort(404)

    page_size = 10
    review_count = users.review_count(user_id)
    page_count = math.ceil(review_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/user/<int:user_id>/1")
    if page > page_count:
        return redirect("/user/<int:user_id>/" + str(page_count))

    items = users.get_reviews(user_id, page, page_size)
    return render_template("show_user.html", count=review_count, user=user, items=items, page=page, page_count=page_count)

@app.route("/search_item")
def search_item():
    query = request.args.get("query")
    if query:
        results = items.search_items(query)
    else:
        query = ""
        results = []
    return render_template("search_item.html", query=query, results=results)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    item = items.get_item(item_id)
    if not item:
        abort(404)
    classes = items.get_classes(item_id)
    comments = items.get_comments(item_id)
    return render_template("show_item.html", item=item, classes=classes, comments=comments)

@app.route("/new_item")
def new_item():
    require_login()
    classes = items.get_all_classes()
    return render_template("new_item.html", classes=classes)

@app.route("/create_item", methods=["POST"])
def create_item():
    require_login()
    check_csrf()
    
    book_name = request.form["book_name"]
    author = request.form["author"]
    grade = request.form["grade"]
    review = request.form["review"]

    if not book_name or not author or not grade or not review:
        abort(403)
    if len(book_name)>30 or len(author)>20 or len(review)>1000:
        abort(403)
    if not re.search(r"10|[1-9]|^([1-9])\.([05])$", grade):
        abort(403)
    user_id = session["user_id"]

    all_classes = items.get_all_classes()
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    items.add_item(book_name, author, grade, review, user_id, classes)
    return redirect("/")

@app.route("/edit_item/<int:item_id>")
def edit_item(item_id):
    require_login()
    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    all_classes = items.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in items.get_classes(item_id):
        classes[entry["title"]] = entry["value"]
        
    return render_template("edit_item.html", item=item, classes=classes, all_classes=all_classes)

@app.route("/update_item", methods=["POST"])
def update_item():
    require_login()
    check_csrf()

    item_id = request.form["item_id"]
    item = items.get_item(item_id)
    if item["user_id"] != session["user_id"]:
        abort(403)

    book_name = request.form["book_name"]
    author = request.form["author"]
    grade = request.form["grade"]
    review = request.form["review"]

    if not book_name or not author or not grade or not review:
        abort(403)
    if len(book_name)>30 or len(author)>20 or len(review)>1000:
        abort(403)
    if not re.search(r"10|[1-9]|^([1-9])\.([05])$", grade):
        abort(403)

    all_classes = items.get_all_classes()
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    items.update_item(item_id, book_name, author, grade, review, classes)

    return redirect("/item/" + str(item_id))

@app.route("/delete_item/<int:item_id>", methods = ["GET", "POST"])
def delete_item(item_id):
    require_login()

    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("delete_item.html", item=item)
    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            items.delete_item(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))

@app.route("/new_comment", methods=["POST"])
def new_comment():
    require_login()
    check_csrf()
    
    comment = request.form["comment"]
    if not  comment:
        abort(403)
    if len(comment)>500:
        abort(403)

    item_id = request.form["item_id"]
    user_id = session["user_id"]

    items.create_comment(item_id, user_id, comment)
    return redirect("/item/" + str(item_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return redirect("/register")
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: tunnus on jo varattu")
        return redirect("/register")
    flash("Uuden käyttäjän luonti onnistui!")
    return redirect("/")

@app.route("/login", methods=["GET","POST"])
def login():
        if request.method == "GET":
            return render_template("login.html")

        if request.method == "POST": 
            username = request.form["username"]
            password = request.form["password"]

            user_id = users.check_login(username, password)
            if user_id:
                session["user_id"] = user_id
                session["username"] = username
                session["csrf_token"] = secrets.token_hex(16)
                flash("Tervetuloa "+username+"!")
                return redirect("/")
            else:
                flash("VIRHE: väärä tunnus tai salasana")
                return redirect("/login")

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")
