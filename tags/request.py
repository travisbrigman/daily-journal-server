from models import Tag, Entry_Tag
import json
import sqlite3

def get_all_tags():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            tags.id,
            tags.subject
        FROM tags 
        """)

        # Initialize an empty list to hold all entry representations
        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entry class above.
            entry = Tag(row['id'], row['subject'])

            tags.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(tags)


def get_all_entries_tags():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.entry_id,
            e.tag_id
        FROM Entries_Tags e 
        """)

        # Initialize an empty list to hold all entry representations
        entries_tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entry class above.
            entry = Entry_Tag(row['id'], row['entry_id'], row['tag_id'])

            entries_tags.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries_tags)