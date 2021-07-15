import sqlite3

VARIANTS = {
    0: 'positive',
    1: 'hesitantly_positive',
    2: 'neutral',
    3: 'negative',
}


def get_table(table):
    with sqlite3.connect('./magialyq/db/database.db') as db:
        result = {}
        cursor = db.cursor()
        sqlite_select_query = """SELECT * from {}""".format(table)
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for key, answer in records:
            result.setdefault(key, answer)
        return result