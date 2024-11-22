import mysql.connector as mc

try:
    # Connect to the MySQL database
    conn = mc.connect(
        host='localhost',
        user='root',
        password='Gudetama-123',
        database='menagerie'
    )
    c = conn.cursor()

    # Describe the 'pet' table
    print("Structure of the 'pet' table:")
    c.execute("DESCRIBE pet;")
    structure = c.fetchall()

    # Display the structure in a formatted table
    print(f"{'Field':<15}{'Type':<20}{'Null':<10}{'Key':<10}{'Default':<15}{'Extra'}")
    print("-" * 70)
    for row in structure:
        print(f"{row[0]:<15}{row[1]:<20}{row[2]:<10}{row[3]:<10}{str(row[4]):<15}{row[5]}")

except mc.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'c' in locals() and c:
        c.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Connection closed.")
