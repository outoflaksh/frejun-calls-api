import sqlite3


def create_call(from_number, to_number):
    try:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS calls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_number CHAR(10) NOT NULL,
            to_number CHAR(10) NOT NULL,
            start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        )

        conn.commit()

        insertion_query = """INSERT INTO calls (from_number, to_number) VALUES (?, ?)"""
        data = (from_number, to_number)
        cursor.execute(insertion_query, data)
        conn.commit()
    except sqlite3.OperationalError or sqlite3.Error:
        raise Exception("Something wrong!")


def get_calls(phone):
    try:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        selection_query = """SELECT * FROM calls WHERE from_number=? OR to_number=?"""
        res = cursor.execute(selection_query, (phone, phone))

        results = []
        for r in res:
            results.append(
                {
                    "id": r[0],
                    "from_number": r[1],
                    "to_number": r[2],
                    "start_time": r[3],
                }
            )

        return results
    except sqlite3.OperationalError:
        raise Exception("Table doesn't exist yet!")
