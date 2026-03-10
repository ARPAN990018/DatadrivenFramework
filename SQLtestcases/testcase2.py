import mysql.connector


con = mysql.connector.connect(user='root',password='Ab@ni123',host='localhost',database='employee')
curs = con.cursor()
curs.execute("select * from employeeDetail")

for row in curs:
    print(row[0],row[1],row[2],row[3])

con.close()