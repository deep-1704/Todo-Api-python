from db_connection import get_db_connection

cnx = get_db_connection()


def get_tasks(username):
    cursor = cnx.cursor()
    query = "SELECT * FROM task WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    cursor.close()
    return result


def get_task(username, task_id):
    cursor = cnx.cursor()
    query = "SELECT * FROM task WHERE username = %s AND id = %s"
    cursor.execute(query, (username, task_id))
    result = cursor.fetchone()
    cursor.close()
    return result


def create_task(username, description):
    cursor = cnx.cursor()
    query = "INSERT INTO task (username, description, status) VALUES (%s, %s, false)"
    cursor.execute(query, (username, description))
    cnx.commit()
    cursor.close()


def update_task_description(username, task_id, description):
    cursor = cnx.cursor()
    query = "UPDATE task SET description = %s WHERE username = %s AND id = %s"
    cursor.execute(query, (description, username, task_id))
    cnx.commit()
    cursor.close()


def update_task_status(username, task_id, status):
    cursor = cnx.cursor()
    query = "UPDATE task SET status = %s WHERE username = %s AND id = %s"
    cursor.execute(query, (status, username, task_id))
    cnx.commit()
    cursor.close()


def delete_task(username, task_id):
    cursor = cnx.cursor()
    query = "DELETE FROM task WHERE username = %s AND id = %s"
    cursor.execute(query, (username, task_id))
    cnx.commit()
    cursor.close()