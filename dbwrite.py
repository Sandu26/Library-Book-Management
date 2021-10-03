import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
def get_books(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM book_register_book")
    rows = cur.fetchall()
    with open("book_list.txt", 'w') as file:
        file.write("Title,Author,Genre,Height,Publisher"+"\n")
    with open("book_list.txt", 'a') as file:
        for row in rows:
            line = ', '.join(row[1:])
            file.write(line+"\n")

def main():
    database = r"C:\\Users\\user\\Desktop\\181452T\\GUI\\LibraryBookManagement_site\\db_books.sqlite3"
    # create a database connection
    conn = create_connection(database)
    with conn:
        get_books(conn)


if __name__ == '__main__': 
    main()
