import sqlite3
from sqlite3 import Error

DATABASE_PATH = "./bot/db/sqlite.db"


def create_connection(db_file):
    """Create a database connection to the SQLite database.

    Args:
        db_file: database file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        return 'Error Establishing a Database Connection'
    return conn


def select_answer(conn, id):
    """Query all rows in the tasks table.

    Args:
        conn: the Connection object
        id: id
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM answers WHERE key == {}".format(id))

    rows = cur.fetchall()

    for item in rows:
        key, answer = item
        return answer


def select_warning(conn, id):
    """Query all rows in the tasks table.

    Args:
        conn: the Connection object
        id: id
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM warnings WHERE key == {}".format(id))

    rows = cur.fetchall()

    for item in rows:
        key, warning = item
        return warning


def select_question(conn, id):
    """Query all rows in the tasks table.

    Args:
        conn: the Connection object
        id: id
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions WHERE key == {}".format(id))

    rows = cur.fetchall()

    for item in rows:
        key, warning = item
        return warning


def main(answer_num, warning_num, question_num):
    conn = create_connection(DATABASE_PATH)
    with conn:
        answer = select_answer(conn, answer_num)

        warning = select_warning(conn, warning_num)

        question = select_question(conn, question_num)

        return answer, warning, question
