import mysql.connector as mc

try:
    # Connect to the MySQL database
    conn = mc.connect(
        host='localhost',
        user='root',
        password='Gudetama-123',  # Replace with your MySQL password
        database='menagerie'     # Ensure the 'menagerie' database exists
    )
    c = conn.cursor()

    # Query to fetch name and birth columns from the 'pet' table
    print("Name and Birth columns from the 'pet' table:")
    c.execute("SELECT name, birth FROM pet;")
    records = c.fetchall()

    # Display the records in a formatted table
    print(f"{'Name':<10}{'Birth':<12}")
    print("-" * 25)
    for row in records:
        name, birth = row
        birth_date = birth.strftime('%Y-%m-%d') if birth else "NULL"  # Format the date properly
        print(f"{name:<10}{birth_date:<12}")

except mc.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'c' in locals() and c:
        c.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Connection closed.")
