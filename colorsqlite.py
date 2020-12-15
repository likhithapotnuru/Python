import sqlite3
from csv import reader

def connect():
    conn = sqlite3.connect("colors.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS colorstable(
               color text,
               colorname text,
               hexcode text,
               R integer,
               G integer,
               B integer)""")
    conn.commit()
    conn.close()

def insert():
    conn = sqlite3.connect("colors.db")
    c = conn.cursor()
    with open('colors.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            c.execute("""INSERT INTO colorstable VALUES(?,?,?,?,?,?)""",(row[0],row[1],row[2],row[3],row[4],row[5]))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("colors.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM colorstable""")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print(rows)
    
def displaycolorname(B,G,R):
    conn = sqlite3.connect("colors.db")
    c = conn.cursor()
    c.execute("""SELECT colorname FROM colorstable WHERE B=? AND G=? AND R=?""",(B,G,R))
    x =  c.fetchone()
    conn.commit()
    conn.close()
    return x

connect()
#insert()
#view()
#displaycolorname(B=0, G=0, R=0)