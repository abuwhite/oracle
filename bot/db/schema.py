import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database.

    Args:
        db_file: database file
    """
    conn = None
    try:
        print("Connected db!", db_file)
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

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
    database = "./bot/db/sqlite.db"

    conn = create_connection(database)
    with conn:
        answer = select_answer(conn, answer_num)
        print("[ANSWER IS SELECTED]", answer)

        warning = select_warning(conn, warning_num)
        print("[WARNING IS SELECTED]", warning)

        question = select_question(conn, question_num)
        print("[QUESTION IS SELECTED]", question)

        return answer, warning, question


if __name__ == "__main__":
    main()
