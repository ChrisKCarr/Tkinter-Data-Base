import sqlite3

def connect():
    conn=sqlite3.connect("tipsdb.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, address text, name text, ord integer, tip integer)")
    conn.commit()
    conn.close()

def insert(address,name,ord,tip):
    conn=sqlite3.connect("tipsdb.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(address,name,ord,tip))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("tipsdb.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(address="",name="",ord="",tip=""):
    conn=sqlite3.connect("tipsdb.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE address=? OR name=? OR ord=? OR tip=?", (address,name,ord,tip))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("tipsdb.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,address,name,ord,tip):
    conn=sqlite3.connect("tipsdb.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET address=?, name=?, ord=?, tip=? WHERE id=?",(address,name,ord,tip,id))
    conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
