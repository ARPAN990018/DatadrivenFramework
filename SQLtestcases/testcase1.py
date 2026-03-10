import mysql.connector
input_Query = "insert into employeeDetail value('John',8,900000,'SDE1')"
update_query = "update employeedetail set employeename='Stalin' where employeename='John'"
Delete_query = "delete from employeedetail where employeename='Stalin'"

con = mysql.connector.connect(user='root', password='Ab@ni123',host='localhost',database='employee')
cur = con.cursor()
#cur.execute(input_Query)
#cur.execute(update_query)
cur.execute(Delete_query)
con.commit()
con.close()


