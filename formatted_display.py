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
    print("+-----------+------------+-------------+")
    print("| Name      | Birth      | Month(birth)|")
    print("+-----------+------------+-------------+")
    c.execute("SELECT name, birth, MONTH(birth) AS birth_month FROM pet;")
    records = c.fetchall()

    # Display the results in a formatted table
    for row in records:
        name, birth, month = row
        birth_date = birth.strftime('%Y-%m-%d') if birth else "NULL"  # Format the date properly
        print(f"| {name:<9} | {birth_date:<10} | {month:<11} |")
    print("+-----------+------------+-------------+")

except mc.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'c' in locals() and c:
        c.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Connection closed.")
