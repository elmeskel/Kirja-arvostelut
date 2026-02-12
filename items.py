import db

def add_item(book_name, author, grade, review, user_id, classes):
    sql = """INSERT INTO items (book_name, author, grade, review, user_id) 
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [book_name, author, grade, review, user_id])
    
    item_id = db.last_insert_id()
    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?,?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def get_classes(item_id):
    sql = "SELECT  title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items():
    sql = "SELECT id, book_name, author, grade FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.book_name,
                    items.author,
                    items.grade,
                    items.review,
                    users.id user_id,
                    users.username
            FROM items, users
            WHERE items.user_id = users.id AND
            items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id,book_name, author, grade, review):
    sql = """UPDATE items   SET book_name = ?,
                                author = ?,
                                grade = ?,
                                review = ?
                            WHERE id == ?"""
    db.execute(sql, [book_name, author, grade, review, item_id])

def delete_item(item_id):
    sql = "DELETE FROM items WHERE id == ?"
    db.execute(sql, [item_id])

def search_items(query):
    sql = """SELECT id, book_name, author, grade
            FROM items
            WHERE book_name LIKE ? OR review LIKE ? OR author LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])