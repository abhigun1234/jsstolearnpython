import mysql.connector
def getConnection():
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="retail"
  )
  print(mydb)
  return  mydb
def getProduct(mydb):

  print('getProduct',mydb)
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM product")

  myresult = mycursor.fetchall()
  print(myresult)

  return  myresult




