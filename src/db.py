import sqlite3


def create_call(from_number, to_number):
    """
    Create a call item in the database with the given arguments.

    from_number: string
    to_number: string
    """
    try:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        # Table creation query
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS calls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_number CHAR(10) NOT NULL,
            to_number CHAR(10) NOT NULL,
            start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        )

        conn.commit()

        # Creating the required record
        insertion_query = """INSERT INTO calls (from_number, to_number) VALUES (?, ?)"""
        data = (from_number, to_number)
        cursor.execute(insertion_query, data)
        conn.commit()
    except sqlite3.OperationalError or sqlite3.Error:
        raise Exception("Something wrong!")


def get_calls(phone):
    """
    Retrieve all calls from the database where the given argument
    exists in either the to_number or from_number column.

    phone: string
    """
    try:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        # Selection query to check for the given phone number
        selection_query = """SELECT * FROM calls WHERE from_number=? OR to_number=?"""
        res = cursor.execute(selection_query, (phone, phone))

        # Formatting records as required
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
