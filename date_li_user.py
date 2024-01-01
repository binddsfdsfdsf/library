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

def insert_user(connection, *values):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO abonnes (NumeroMatricule ,Nom ,Prenom, Adresse,Email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, values)
        connection.commit()
        print("user inserted successfully")
    except Error as e:
        print(f"Error: {e}")
    
def select_all_user(connection):

    try:
            cursor = connection.cursor()
            query = "SELECT * FROM abonnes"
            cursor.execute(query)
            books = cursor.fetchall()
            close_connection(connection)
            book1=[["Name", "User ID", "First name", "Date of birth", "Email"],]
            for book in books:
                book1.append(list(book))
            return book1
    except Error as e:
        print(f"Error: {e}")
def update_user(connection, code_catalogue, *new_values):
# def update_book(connection, code_catalogue, *new_values):
    try:
        cursor = connection.cursor()
        query = "UPDATE abonnes SET Nom=%s, Prenom=%s, Adresse=%s, Email=%s WHERE NumeroMatricule=%s"
        cursor.execute(query, (*new_values, code_catalogue))
        connection.commit()
        print("User updated successfully")
    except Error as e :

        print(f"Error: {e}")

    # ["NumeroMatricule","Nom" ,"Prenom"," Adresse"," Email"]
    # try:
    #     cursor = connection.cursor()
    #     query = "UPDATE abonnes SET Nom=%s, Prenom=%s, Adresse=%s, Email=%s WHERE NumeroMatricule=%s"
    #     cursor.execute(query, (*new_values, code_catalogue))
    #     connection.commit()
    #     print("user updated successfully")
    # except Error as e :

    #     print(f"Error: {e}")

def delete_user(connection, code_catalogue):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM abonnes WHERE NumeroMatricule=%s"
        cursor.execute(delete_query, (code_catalogue,))
        connection.commit()

    except Error as e:
        print(f"Error: {e}")

def search_user(connection, title):
    if not title:
        return None

    try:
        cursor = connection.cursor()
        WHERE =["Nom" ,"Prenom"," Adresse"," Email"]
        search_results = []

        for i in WHERE:
            query = f"SELECT * FROM abonnes WHERE {i} LIKE %s"
            cursor.execute(query, ('%' + title + '%',))
            search_results.extend(cursor.fetchall())

        if not search_results:
            print("No matching books found.")
        else:
            print("Search Results:")
            return [["Title", "Book ID", "Author", "Publisher", "category"]] + [list(book) for book in search_results]

    except Error as e:
        print(f"Error: {e}")
        return None
# con=create_connection()
# print(search_user(con,""))
