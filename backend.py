import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    con.commit()
    con.close()
    
def insert(title,author,year,isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()
    
def view():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    row=cur.fetchall()
    con.close()
    
    return row

def search(title="",author="",year="",isbn=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    row=cur.fetchall()
    con.close()
    
    return row

def delete(title):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE title=?",(title,))
    con.commit()
    con.close()
    
    
connect()