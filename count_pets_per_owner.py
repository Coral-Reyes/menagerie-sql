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

    # Query to count the number of pets for each owner
    print("Number of pets each owner has:")
    c.execute("SELECT owner, COUNT(*) AS num_pets FROM pet GROUP BY owner;")
    records = c.fetchall()

    # Display the results in a formatted table
    print(f"{'Owner':<15}{'Number of Pets':<15}")
    print("-" * 30)
    for row in records:
        owner, num_pets = row
        print(f"{owner:<15}{num_pets:<15}")

except mc.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'c' in locals() and c:
        c.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Connection closed.")
