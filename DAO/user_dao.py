from db_connection import get_db_connection

cnx = get_db_connection()


def get_user_by_username(username):
    cursor = cnx.cursor()
    query = "SELECT * FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    return result


def create_user(username, password):
    cursor = cnx.cursor()
    query = "INSERT INTO user (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    cnx.commit()
    cursor.close()


