import mysql.connector

try:
    connection = mysql.connector.connect(host = 'localhost',database = 'connector',user = 'root', password = 'root')

except:
    print("something went wrong")    