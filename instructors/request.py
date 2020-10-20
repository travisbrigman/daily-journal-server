from models import Instructor
import json
import sqlite3

def get_all_instructors():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            i.id,
            i.first_name,
            i.last_name

        FROM Instructors i
        """)

        # Initialize an empty list to hold all instructor representations
        instructors = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an instructor instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # instructor class above.
            instructor = Instructor(row['id'], row['first_name'], row['last_name'])

            instructors.append(instructor.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(instructors)