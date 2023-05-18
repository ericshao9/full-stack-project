import mysql.connector as sql

conn = sql.connect(host="localhost", user="root")
cur = conn.cursor()

# Test connection
print(conn)

cur.execute("CREATE USER 'flask'@'localhost' IDENTIFIED BY 'ubuntu';")

cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'flask'@'localhost' WITH GRANT OPTION;")

cur.execute("FLUSH PRIVILEGES;")

conn.close()