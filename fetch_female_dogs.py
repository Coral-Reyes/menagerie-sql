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

    # Query to fetch records of female dogs
    print("Records of female dogs in the 'pet' table:")
    c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
    records = c.fetchall()

    # Display the records in a formatted table
    print(f"{'Name':<10}{'Owner':<10}{'Species':<10}{'Sex':<5}{'Birth':<12}{'Death':<12}")
    print("-" * 60)
    for row in records:
        name, owner, species, sex, birth, death = row
        print(f"{name:<10}{owner:<10}{species:<10}{sex:<5}{birth or 'NULL':<12}{death or 'NULL':<12}")

except mc.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'c' in locals() and c:
        c.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Connection closed.")
