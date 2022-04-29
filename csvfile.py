#!/usr/bin python
import sqlite3 as sql
import os
import csv
from sqlite3 import Error

try:

  
  conn=sql.connect('mydb.db')

  conn.execute('''CREATE TABLE IF NOT EXISTS Employee(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
               Name TEXT NOT NULL, Salary INT NOT NULL
              );''')
  
  conn.execute('''INSERT INTO Employee(Name, Salary) VALUES('Arvind', 80000);''')
  conn.execute('''INSERT INTO Employee(Name, Salary) VALUES('Dishu', 100000);''')
  
  conn.commit()

 
  print ("**Employee Table Data**")
  cur = conn.cursor()
  cur.execute('''SELECT * FROM Employee''')
  rows = cur.fetchall()

  for row in rows:
      print(row)

 
  print ("Exporting data into CSV...")
  cursor = conn.cursor()
  cursor.execute("select * from Employee")
  with open("employee_data.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter="\t")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)

  dirpath = os.getcwd() + "/employee_data.csv"
  print ("Data exported Successfully into {}.format(dirpath)")

except Error as e:
  print(e)

# Close database connection
finally:
  conn.close()
