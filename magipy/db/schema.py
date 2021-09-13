import sqlite3
import os

VARIANTS = {
    0: "positive",
    1: "hesitantly_positive",
    2: "neutral",
    3: "negative",
}
dir = os.path.abspath(__file__)
print(dir)
path = os.path.join(dir, "database.db")
print(path)


def get_table(table):
    print(path)
    with sqlite3.connect(path) as db:
        result = {}
        cursor = db.cursor()
        sqlite_select_query = """SELECT * from {}""".format(table)
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for key, answer in records:
            result.setdefault(key, answer)
        return result
