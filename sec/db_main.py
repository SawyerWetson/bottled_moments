import sqlite3
import os
import sys

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
# Note: UNIQUE CHAR is not a valid SQLite data type. TEXT or VARCHAR is more appropriate.
# AUTOINCREMENT is typically used with INTEGER PRIMARY KEY.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bottlestock_small INTEGER NOT NULL,
        bottlestock_large INTEGER NOT NULL,
        bottlestock_special TEXT UNIQUE
    )
''')
conn.commit() # Commit the table creation

def main():
    # Example data to insert
    bottlestock_small_val = 100 # Example integer value
    bottlestock_large_val = 50  # Example integer value
    bottlestock_special_val = "Limited Edition" # Example text value

    # Insert data into the table
    try:
        cursor.execute('''
            INSERT INTO inventory (bottlestock_small, bottlestock_large, bottlestock_special)
            VALUES (?, ?, ?)
        ''', (bottlestock_small_val, bottlestock_large_val, bottlestock_special_val))
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting data: {e}. The 'bottlestock_special' value might not be unique.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # You can also retrieve data here if needed
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    print("\nCurrent inventory:")
    for row in rows:
        print(row)

    # Close the connection when done
    conn.close()

if __name__ == "__main__":
    main()
