# library seems to be common and native
import sqlite3

# creates the intended file - similar to touch
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# create the table
conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")

conn.close()

#-------------------------------------------------

# execute and commit methods - lets define a function instead
def open_sqllite_db(file):
    conn = sqlite3.connect(file)
    print("Opened database successfully")
    return conn

file = 'test.db'

conn = open_sqllite_db(file)


conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records created successfully")
conn.close()

#-------------------------------------------------

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print( "ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()

#-------------------------------------------------

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

# do a sql statement
cursor = conn.execute("SELECT id, name, address, salary from COMPANY where NAME='Paul'")

# create a list of the said object
for row in cursor:
    print(row)
    print(row[0], row[1], row[2], row[3])