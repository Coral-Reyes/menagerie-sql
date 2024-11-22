import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Gudetama-123')
c = conn.cursor()

c.execute('SHOW DATABASES;')
databases = c.fetchall()
for db in databases:
    print(db)
