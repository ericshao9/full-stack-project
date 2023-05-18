from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/order')
def order():
    return render_template("order.html")

@app.route('/update',methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        try:
            Pork = request.form['Pork']
            Beef = request.form['Beef']
            Shrimp = request.form['Shrimp']
            Mushroom = request.form['Mushroom']
            ScallionP = request.form['ScallionP']

            with sql.connect(host="localhost", \
                    user="flask", \
                    password="ubuntu", \
                    database="restaurant_db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Food (Pork,Beef,Shrimp,Mushroom,ScallionP) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(Pork,Beef,Shrimp,Mushroom,ScallionP))
                con.commit()
                msg = "Order successfully placed! The chef will start cooking now."
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html",msg = msg)
            con.close()
    
@app.route('/chef')
def chef():
    with sql.connect(host="localhost", \
                    user="flask", \
                    password="ubuntu", \
                    database="restaurant_db") as con:
        
        cur = con.cursor()
        cur.execute("Select * from Food")
        rows = cur.fetchall()
    return render_template("chef.html",rows = rows)

if __name__ == '__main__':
    app.run(debug=True)
