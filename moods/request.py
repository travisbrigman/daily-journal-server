from models import Mood
import sqlite3
import json

def get_all_moods():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            id,
            label
        FROM moods 
        """)

        # Initialize an empty list to hold all entry representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entry class above.
            entry = Mood(row['id'], row['label'])

            moods.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(moods)