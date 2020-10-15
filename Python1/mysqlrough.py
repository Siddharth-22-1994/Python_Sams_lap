# from datetime import datetime
# import mysql.connector

# Db = mysql.connector.connect(
#     user='root',
#     host='localhost',
#     passwd='root'
#     # database='Customers'
# )

# print(Db)

# mycursor = Db.cursor()

# # now = datetime.now()
# # id = 1
# # formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

# mycursor.execute("CREATE DATABASE Customers")

# mycursor.execute('CREATE TABLE custdetails(Name VARCHAR(50), Id VARCHAR(20) PRIMARY KEY NOT NULL, Phone VARCHAR(13), TIME VARCHAR(60), Place VARCHAR(50), Points VARCHAR(10))')

# sqlformula = "INSERT INTO custdetails(Name, Id, Phone, TIME, Place, Points) VALUES(%s, %s, %s, %s, %s, %s)"
# cust1 = [('Hithu', '1', '9456745345', formatted_date, 'Banglore', '200'),
#          ('Jinu', '2', '8763245623', formatted_date, 'Hydrabed', '350'),
#          ('Tofi', '3', '2456746534', formatted_date, 'Coimbatore', '190'),
#          ('Yugy', '4', '9876543234', formatted_date, 'Banglore', '150'),
#           ('Toju', '5', '9087654568', formatted_date, 'City', '500')]
#
# mycursor.executemany(sqlformula, cust1)
# Db.commit()

# mycursor.execute("SELECT Name, Id, 'Bronze' AS Type FROM custdetails WHERE Points <=200 UNION SELECT Name, Id, 'Silver' AS Type FROM custdetails WHERE Points BETWEEN 201 AND 350 UNION SELECT Name, Id, 'Gold' AS Type FROM custdetails WHERE Points >400")
#
#
# for val in mycursor:
#    print(val)

# mycursor.execute('SELECT Name FROM custpersonaldetails')
# res = mycursor.fetchmany(2)
# for row in res:
#     print(row)
# # print(res)
