import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE isecure")
mycursor.execute("SHOW DATABASES")

mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  database="isecure"
)

mycursor1 = mydb1.cursor()
mycursor1.execute("CREATE TABLE logindb (ID INT(11), Username TEXT, Password TEXT, API TEXT, Directory TEXT, Camera TEXT, RTSP TEXT)")
mycursor1.execute("SHOW TABLES")