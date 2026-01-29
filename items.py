import db

def add_item(book_name, author, grade, review, user_id):
    
    sql = """INSERT INTO items (book_name, author, grade, review, user_id) 
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [book_name, author, grade, review, user_id])

def get_items():
    sql = "SELECT id, book_name, author, grade FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.book_name,
                    items.author,
                    items.grade,
                    items.review,
                    users.username
            FROM items, users
            WHERE items.user_id = users.id AND
            items.id = ?"""
    return db.query(sql, [item_id])[0]