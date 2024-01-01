import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='library',
            user='root',
            password='1234'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed")

def insert_book(connection, *values):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Livres (CodeCatalogue, Titre, Auteur, Editeur, Theme) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, values)
        connection.commit()
        print("Book inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def select_all_books(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Livres"
        cursor.execute(query)
        books = cursor.fetchall()
        close_connection(connection)
        book1=[["Title","Book ID", "Author", "Publisher", "category"],]
        for book in books:
            book1.append(list(book))
        return book1
    except Error as e:
        print(f"Error: {e}")

def update_book(connection, code_catalogue, *new_values):
    try:
        cursor = connection.cursor()
        query = "UPDATE Livres SET Titre=%s, Auteur=%s, Editeur=%s, Theme=%s WHERE CodeCatalogue=%s"
        cursor.execute(query, (*new_values, code_catalogue))
        connection.commit()
        print("Book updated successfully")
    except Error as e :

        print(f"Error: {e}")

def delete_book(connection, code_catalogue):
    try:
        cursor = connection.cursor()

        original_order_query = "SELECT CodeCatalogue FROM Livres ORDER BY CodeCatalogue"
        cursor.execute(original_order_query)
        original_order = [row[0] for row in cursor.fetchall()]
        print(original_order)
        delete_query = "DELETE FROM Livres WHERE CodeCatalogue=%s"
        cursor.execute(delete_query, (code_catalogue,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def search_book(connection, title):
    if not title:
        return None

    try:
        cursor = connection.cursor()
        WHERE = ["Titre", "Auteur", "Editeur", "Theme"]
        search_results = []

        for i in WHERE:
            query = f"SELECT * FROM Livres WHERE {i} LIKE %s"
            cursor.execute(query, ('%' + title + '%',))
            search_results.extend(cursor.fetchall())
            if search_results:
                break

        if not search_results:
            print("No matching books found.")
        else:
            print("Search Results:")
            return [["Title", "Book ID", "Author", "Publisher", "category"]] + [list(book) for book in search_results]

    except Error as e:
        print(f"Error: {e}")
        return None

con=create_connection()
print(search_book(con,"T"))
 