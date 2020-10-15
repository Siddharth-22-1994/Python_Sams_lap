# Source code to link Python and Mysql
# 		Proper Guide
                     # Note : To Execute - Ctrl + Shift + r
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="!S@#id199$4",
    database='TestDb',
)
print(mydb)

mycursor = mydb.cursor()

# Step 1:
# mycursor.execute('CREATE DATABASE TestDb')

# Step 2:
# To show the databses

# mycursor.execute('SHOW DATABASES')
#
# for db in mycursor:
#     print(db)

# Step 3:
# Add database to = config (see above), This is used to use the particulart Database.

# Step 4:
# Create a table
# mycursor.execute('CREATE TABLE Students(Name VARCHAR(50), Age INTEGER(10))')

# Step 5:
# To show the tables in our database

# mycursor.execute('SHOW TABLES')
#
# for db in mycursor:
#     print(db)

# Step 6:
# To Populate the Table - To do that create a sqlFormula

# sqlFormula = "INSERT INTO Students(Name, Age) VALUES (%s, %s)"
# This method is to add ONE value and Execute it
# Student1 = ('Rachel', '25')
# mycursor.execute(sqlFormula, Student1)

# Inorder method to add BUNCH of values and Execute it
# Student1 = [("Bob", "24"),
#             ("Lisa", "22"),
#             ("Migu", "14"),
#             ("Clare", "28"),
#             ("Alies", "30"),]
#
# mycursor.executemany(sqlFormula, Student1)  [NOTE: use executemany to add many Items]
#             # (Note: This command help to make changes in our table)
# mydb.commit()

# Step 7:
# To select the ALL the data and fetch the datas in Table (fetchall() is used)
# mycursor.execute('SELECT * FROM Students')
# or
# mycursor.execute('SELECT Age FROM Students')
# myresult = mycursor.fetchall()
#
# for row in myresult:
#     print(row)

# To select the ONLY ONE data and fetch the datas in Table (fetchone() is used)
# mycursor.execute('SELECT age FROM Students')
# myresult = mycursor.fetchone()
#
# for row in myresult:
#     print(row)

# To select the number of userwished data and fetch the datas in Table (fetchmany(3) is used)
# mycursor.execute('SELECT age FROM Students')
# myresult = mycursor.fetchmany(3)
#
# for row in myresult:
#     print(row)

# Step 8:
# To Use WHERE command

# sql = 'SELECT * FROM Students WHERE Age=25'
# or
# sql = "SELECT * FROM Students WHERE Name='Lisa'"
#
# mycursor.execute(sql)
# myresults = mycursor.fetchall()
#
# for result in myresults:
#     print(result)

# Step 9:
# To Use WHILECARD Characters(Eg: LIKE...)

# sql = "SELECT * FROM Students WHERE Name LIKE 'Cl%'"
# mycursor.execute(sql)
# To Use 'NOT' Operator With LIKE
# mycursor.execute("STUDENTS * FROM Students WHERE Name NOT LIKE '%a' ")
# or(Best to use PlaceHolders)
# sql = "SELECT * FROM Students WHERE Name = %s"
#
# mycursor.execute(sql, ("Migu", ))
#             # rest all the steps are same
# myresult = mycursor.fetchall()
#
# for results in myresult:
#     print(results)

# Step 10:
# To use UPDATE
# sql = "UPDATE Students SET Age=30 WHERE Name='Lisa'"
#
# mycursor.execute(sql)
# mydb.commit()
# mydb.commit()

# To use LIMIT
# mycursor.execute("SELECT * FROM Students LIMIT 4")
# or To select from Inbetween valus
# mycursor.execute("SELECT *FROM Students LIMIT 3 OFFSET 2")
# myresult = mycursor.fetchall()
#
# for val in myresult:
#     print(val)

# Step 11
# To use ORDER BY Ascending oredr
# sql = "SELECT * FROM Students ORDER BY Age"

# or To use ORDER BY Descending oredr
# sql = "SELECT * FROM Students ORDER BY Age DESC"
#
# mycursor.execute(sql)
#
# Result = mycursor.fetchall()
#
# for r in Result:
#     print(r)

# Step 12
# To DELETE an Item from Table
# sql = "DELETE FROM Students WHERE Age=25"
#
# mycursor.execute(sql)
# mydb.commit()

# Step 13
# To DROP TABLE
# sql = "DROP TABLE Students"
#                    # or Best way to DROP Table
# sql = "DROP TABLE IF EXISTS Students"
# mycursor.execute(sql)
# mydb.commit()

# FROM MASH HAMADHANI

# Using "Select Distinct" Keyword (To Eleiminate Duplicate Items)
# Step 14
# mycursor.execute("SELECT DISTINCT Age FROM Students")
#
# for r in mycursor:
#     print(r)

# Step 15
# To create New column using existing column

# mycursor.execute("SELECT Name, Age, Age+10 AS 'NEW_Age' FROM Students")
#
# result = mycursor.fetchall()
#
# for r in result:
#     print(r)

# Step 16
# By Using AND, OR, NOT
# AND
# mycursor.execute("SELECT * FROM Students WHERE Name = 'L%' AND Age > 20 OR (Aa per any field)")
# OR
# mycursor.execute("SELECT * FROM Students WHERE Name = 'L%' OR Age > 20")
# NOT
# mycursor.execute("SELECT * FROM Students WHERE Name LIKE 'L%' NOT Age > 20")

# mycursor.execute("SELECT * FROM Students WHERE NOT(Name LIKE 'L%' OR Age > 20)")


# for db in mycursor:
#     print(db)

# Step 17
# Using IN Operator

# mycursor.execute("SELECT * FROM Students WHERE Age = 24 OR Age = 22")
# Insted, Use IN
# mycursor.execute("SELECT * FROM Students WHERE Age IN('24', '22')")
# To Use IN with NOT
# mycursor.execute("SELECT * FROM Students WHERE Age NOT IN('24', '22')")
#
# for r in mycursor:
#     print(r)

# Step 18
# Using BEWTEEN Opertor

# mycursor.execute("SELECT * FROM Students WHERE Age BETWEEN 20 AND 30")
#
# result = mycursor.fetchall()
#
# for r in result:
#     print(r)

# Step 19
# A best replace for LIKE operator is REGEXP
# mycursor.execute("SELECT * FROM Students WHERE Name REGEXP 'is'") [ Equal to WHERE Name LIKE '%is%']
#                     Another method
# mycursor.execute("SELECT * FROM Students WHERE Name REGEXP 'isa|igu' ") (OR Operation)
# Another method
# mycursor.execute("SELECT * FROM Students WHERE Name REGEXP '[gei]u' ") (OR Operation) or  REGEXP '[a-h]u'
# It will check for the Name which has [gu, eu, iu]

# (^field) means it show the name should start with field
# (field$) means it show the name should end with field
# result = mycursor.fetchall()
#
# for val in result:
#     print(val)

# Step 20
# NULL OPERATOR
# mycursor.execute("SELECT * FROM Students WHERE Name IS NULL")  or Name IS NOT NULL

# for val in mycursor:
#     print(val)

# IMP Topics
#                                         # Step 21
#                                     Using JOIN or INNER JOIN
#                     # Task: This task is to perform taskes with Tables  Order and Customers
# mycursor.execute("SELECT * FROM Orders JOIN Customers ON Orders.customer_id = Customers.customer_id")
#                                  or
# mycursor.execute("SELECT * FROM Orders O JOIN Customers C ON O.customer_id = C.customer_id")
#
# result = mycursor.fetchall()
#
# for val in result:
#     print(val)

# Step 22
# Using Self-Join
# NOTE : The combining fields should not be same
# mycursor.execute("SELECT e.employee_id, e.first_name, m.first_name FROM employees e JOIN employees m ON e.report_to = m.employee_id")
#                                               or
# mycursor.execute("SELECT e.employee_id, e.first_name, m.first_name FROM employees e JOIN employees m ON e.report_to = m.employee_id")
#
# for val in mycursor:
#     print(val)

# Step 23
# Using CompoundJoin
# [This is mostly used when the table has two primary key column]
# mycursor.execute("SELECT * FROM order_items oi JOIN order_item_otes oin ON oi.customet_id=oin.customer_id AND oi.product_id=oin.product_id")
#
# result = mycursor.fetchall()
# for val in result:
#     print(val)

# Step 24
# Join Multiple tables
# mycursor.execute("SELECT * FROM orders O JOIN customers C ON O.customer_id = C.customers_id
#                    JOIN Order_statuses OS ON O.status = OS.order_status_id ORDER BY C.customer_id)
# or
# mycursor.execute("SELECT O.order_id, O.order_date, c.first_name, OS.name AS status FROM orders O JOIN customers C ON O.customer_id = C.customers_id
#                    JOIN Order_statuses OS ON O.status = OS.order_status_id)
# result = mycursor.fetchall()
#
# for val in results:
#     print(val)

# Step 25
# Outer Join
# Divided to two as LEFT JOIN and RIGHT JOIN
# mycursor.execute("SELECT * FROM orders O LEFT JOIN customers C ON C.customer_id = O.customer_id ORDER BY C.customer_id") [It will join table based on left side Table]
# or
# mycursor.execute("SELECT * FROM orders O RIGHT JOIN customers C ON C.customer_id = O.customer_id ORDER BY C.customer_id") [It will join table based on right side Table]

# Step 26
# USING keyword
# mycursor.execute('SELECT * FROM orders O JOIN customers C ON O.customer_id = C.customer_id')
#         # Insted of using ON, we can use USING (in case the column names of the two tables are same)
# mycursor.execute("SELECT * FROM ordes O JOIN customers C USING customer_id")
#
# for val in mycursor:
#     print(val)

# Step 27
# NATURAL JOIN (Not Recomended)
# NOTE: # This will automatically check for the similar column-names in both tables and Join it
# mycursor.execute("SELECT * FROM orders O NATURAL JOIN customers C")
#
# result = mycursor.fetchall()
#
# for val in result:
#     print(val)

# Step 28
# CROSS JOIN
# NOTE: This will join allthe columns from both tables
# mycursor.execute("SELECT * FROM orders O CROSS JOIN customers C ORDER BY C.costomer_id")
#                                                 or
# mycursor.execute("SELECT * FROM oredrs O, ccustomers C ORDER BY C.customer_id")
#
# for val in mycursor:
#     print(val)

# Step 29
# using UNION
# NOTE: This is used to combine records of same or diff tables
# IMP NOTE: The num of Columns should be equal
# mycursor.execute("SELECT * FROM orders WHERE order_date > '2019-01-01' 'ACTIVE' AS Status
#                   UNION
#                   "SELECT * FROM orders WHERE order_date < '2019-01-01' 'Archived' AS Staus")
#
# mycursor.fetchall()
#
# for val in mycursor:
#     print(val)

# Another Example
# mycursor.execute("SELECT customer_id, first_name, points, 'Bronz' AS Type FROM customers WHERE points < 2000
#                  UNION
#                  SELECT customer_id, first_name, points, 'Silver' AS Type FROM customers WHERE points BETWEEN 2000 AND 3000
#                  UNION
#                  SELECT customer_id, first_name, points, 'GOLD' AS Type FROM customers WHERE points > 3000 ORDER BY first_name")
#
# result = mycursor.fetchall()
# for val in result:
#     print(val)
