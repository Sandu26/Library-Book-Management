import sqlite3
from sqlite3 import Error

def file_read(file):   
    content = file.read()
    books = content.split("\n")
    books_cleaned = []
    for book_line in books:
        books_cleaned.append(book_line.split(","))
    books_joined_names = []
    for i,book in enumerate(books_cleaned):
        new_book = []
        word=''
        if i==0:
            continue
        full_word = True
        for index,element in enumerate(book):
            element = element.strip()
            if len(element)>0:
                if element[0]=='"':
                    full_word = False
                    word+=element[1:]
                elif element[-1]=='"':
                    word+=" "+element[:-1]
                    full_word = True
                    new_book.append(word)
                    word = ''
                else:
                    if full_word:
                        new_book.append(element) 
                    else:
                        word+=" "+element
            else:
                new_book.append(element)
        books_joined_names.append(new_book)
    return books_joined_names

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_book(conn, book):
    #DELETE SQL TABLE
    #sql_delete_table="DROP TABLE  book_register_book"
    #cur = conn.cursor()
    #cur.execute(sql_delete_table)
    #conn.commit()

    #CREATE SQL TABLE
    #sql_create_table="CREATE TABLE IF NOT EXISTS book_register_book(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE,author TEXT NOT NULL ,genre TEXT NOT NULL,height TEXT,publisher TEXT NOT NULL)"
    #cur = conn.cursor()
    #cur.execute(sql_create_table)
    #conn.commit()

    #INSERT INTO SQL TABLE
    sql = "INSERT OR REPLACE INTO book_register_book(name,author,genre,height,publisher) VALUES(?,?,?,?,?) "
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()

def get_books(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM book_register_book")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = r"C:\\Users\\user\\Desktop\\181452T\\GUI\\LibraryBookManagement_site\\db_books.sqlite3"
    file = open("books_list.txt", "r+")
    # create a database connection
    books = file_read(file)
    conn = create_connection(database)
    
         
    with conn:
        for book in books[0:]:
            print(book)
            create_book(conn,book)
        get_books(conn)

if __name__ == '__main__':
    main()
