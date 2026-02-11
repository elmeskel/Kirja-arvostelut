import db

def get_user(user_id):
    sql = "SELECT id, username from users WHERE id = ?"
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_reviews(user_id):
    sql = """SELECT id, book_name, author, grade
            FROM items WHERE user_id = ?
            ORDER BY id DESC"""
    return db.query(sql, [user_id])
