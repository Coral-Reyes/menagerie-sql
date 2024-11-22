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

    # Query to fetch name, birth, and MONTH(birth) from the 'pet' table
    print("Name, Birth, and Month of Birth from the 'pet' table:")
    c.execute("SELECT name, birth, MONTH(birth) AS birth_month FROM pet;")
    records = c.fetchall()

    # Display the results in a formatted table
    print(f"{'Name':<10}{'Birth':<12}{'Month(birth)'}")
    print("-" * 30)
    for row in records:
        name, birth, month = row
        birth_date = birth.strftime('%Y-%m-%d') if birth else "NULL"  # Format the date properly
        print(f"{name:<10}{birth_date:<12}{month:<12}")

except mc.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'c' in locals() and c:
        c.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Connection closed.")
