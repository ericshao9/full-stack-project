import mysql.connector as sql
conn = sql.connect(host="localhost", user="flask", password="ubuntu")
cur = conn.cursor()

cur.execute("CREATE DATABASE restaurant_db")
conn.close()

