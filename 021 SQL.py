import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd = "Shankar22@")

print(mydb)

cursor = mydb.cursor()

cursor.execute("Show Databases")

print(cursor.fetchall())
