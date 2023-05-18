import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="restaurant_db")
cur = conn.cursor()

cmd = "CREATE TABLE Food (\
    sid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    Pork VARCHAR(30) NOT NULL,\
    Beef VARCHAR(30), \
    Shrimp VARCHAR(30), \
    Mushroom VARCHAR(30), \
    ScallionP VARCHAR(30))"

cur.execute(cmd)
conn.close()