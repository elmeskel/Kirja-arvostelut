import db

def add_item(book_name, author, grade, review, user_id):
    
    sql = """INSERT INTO items (book_name, author, grade, review, user_id) 
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [book_name, author, grade, review, user_id])