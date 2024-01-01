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

def insert_borrow(connection, *values):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO prets (Cote,NumeroMatricule,CodeCatalogue) VALUES (%s, %s, %s)"
        cursor.execute(query, values)
        connection.commit()
        print("borrow inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def select_all_borrows(connection):
    try:
        cursor = connection.cursor()
        query = """
            SELECT
                p.NumeroMatricule AS `User ID`,
                a.Nom AS `User`,
                p.Cote AS `Book ID`,
                l.Titre AS `Book`,
                p.CodeCatalogue,
                p.DatePret,
                p.DateRetourPrevu
            FROM
                prets p
            JOIN
                abonnes a ON p.NumeroMatricule = a.NumeroMatricule
            JOIN
                livres l ON p.CodeCatalogue = l.CodeCatalogue;
        """
        cursor.execute(query)
        borrows = cursor.fetchall()
        close_connection(connection)

        borrow1 = [
            ["User ID", "User", "Book ID", "Book", "CodeCatalogue", "DatePret", "DateRetourPrevu"],
        ]
        for borrow in borrows:
            borrow1.append(list(borrow))
        return borrow1
    except Error as e:
        print(f"Error: {e}")


def delete_borrow(connection, code_catalogue):
    try:
        cursor = connection.cursor()

        original_order_query = "SELECT CodeCatalogue FROM prets ORDER BY CodeCatalogue"
        cursor.execute(original_order_query)
        original_order = [row[0] for row in cursor.fetchall()]
        print(original_order)
        delete_query = "DELETE FROM prets WHERE CodeCatalogue=%s"
        cursor.execute(delete_query, (code_catalogue,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def search_borrow(connection, title):
    if not title:
        return None

    try:
        cursor = connection.cursor()
        WHERE = ["Titre", "Auteur", "Editeur", "Theme"]
        search_results = []

        for i in WHERE:
            query = f"SELECT * FROM prets WHERE {i} LIKE %s"
            cursor.execute(query, ('%' + title + '%',))
            search_results.extend(cursor.fetchall())
            if search_results:
                break

        if not search_results:
            print("No matching borrows found.")
        else:
            print("Search Results:")
            return [["Title", "borrow ID", "Author", "Publisher", "category"]] + [list(borrow) for borrow in search_results]

    except Error as e:
        print(f"Error: {e}")
        return None
con=create_connection()
print(select_all_borrows(con))
 