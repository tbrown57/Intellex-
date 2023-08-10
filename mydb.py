import mysql.connector

dataBase = mysql.connector.connect(

	host = 'localhost',
	user = 'root',
	passwd = 'password'

	)

#prepare a cursor object
cursorObject = dataBase.cursor()

# Create A Database 
cursorObject.execute("CREATE DATABASE customer")

print("All Done!")