import sqlite3

# Create a new SQLite database (or connect to it)
def create_db():
    conn = sqlite3.connect('users.db')  # This will create a database file named 'users.db'
    cursor = conn.cursor()

    # Create a table to store phone numbers and usernames
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            phone_number TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database and table
create_db()
