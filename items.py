import db

def item_count():
    sql = "SELECT COUNT(*) FROM items"
    return db.query(sql)[0][0]

def get_all_classes():
    sql = "SELECT  title, value FROM classes ORDER BY id"
    result = db.query(sql)
    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)
    return classes

def add_item(book_name, author, grade, review, user_id, classes):
    sql = """INSERT INTO items (book_name, author, grade, review, user_id) 
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [book_name, author, grade, review, user_id])
    
    item_id = db.last_insert_id()
    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?,?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def create_comment(item_id, user_id, comment):
    sql = "INSERT INTO comments (item_id, user_id, comment) VALUES (?,?, ?)"
    db.execute(sql, [item_id, user_id, comment])

def get_comments(item_id):
    sql = """SELECT comments.comment, users.id user_id, users.username
            FROM comments, users
            WHERE comments.item_id = ? AND comments.user_id = users.id
            ORDER BY comments.id DESC"""
    return db.query(sql, [item_id])

def get_classes(item_id):
    sql = "SELECT  title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items(page, page_size):
    sql = """SELECT items.id, items.book_name, items.author,
            items.grade, users.id user_id, users.username,
            COUNT(comments.id) comment_count
            FROM items JOIN users ON items.user_id = users.id
                        LEFT JOIN comments ON items.id = comments.item_id
            GROUP BY items.id
            ORDER BY items.id DESC
            LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

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

def update_item(item_id,book_name, author, grade, review, classes):
    sql = """UPDATE items   SET book_name = ?,
                                author = ?,
                                grade = ?,
                                review = ?
                            WHERE id == ?"""
    db.execute(sql, [book_name, author, grade, review, item_id])
    
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    
    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for class_title, class_value in classes:
        db.execute(sql, [item_id, class_title, class_value])

def delete_item(item_id):
    sql = "DELETE FROM comments WHERE item_id == ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM item_classes WHERE item_id == ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id == ?"
    db.execute(sql, [item_id])

def search_items(query):
    sql = """SELECT id, book_name, author, grade
            FROM items
            WHERE book_name LIKE ? OR review LIKE ? OR author LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])