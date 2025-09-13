import sqlite3

## connect to sqlite
connection = sqlite3.connect('student.db')

## create a cursor object to insert, record and create tables
cursor = connection.cursor()

## creating a table
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""

cursor.execute(table_info)

## Inserting records to table
cursor.execute('''INSERT INTO STUDENT values('John', 'Computer Science', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT values('Emily', 'Physics', 'A', 95)''')
cursor.execute('''INSERT INTO STUDENT values('Michael', 'Biology', 'C', 78)''')
cursor.execute('''INSERT INTO STUDENT values('Jessica', 'History', 'A', 92)''')
cursor.execute('''INSERT INTO STUDENT values('Daniel', 'Chemistry', 'B', 88)''')
cursor.execute('''INSERT INTO STUDENT values('Sarah', 'Mathematics', 'B', 81)''')
cursor.execute('''INSERT INTO STUDENT values('Ryan', 'English Literature', 'A', 98)''')
cursor.execute('''INSERT INTO STUDENT values('Sophia', 'Art and Design', 'C', 75)''')
cursor.execute('''INSERT INTO STUDENT values('David', 'Economics', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT values('Olivia', 'Sociology', 'B', 83)''')

## display all the record
print('The inserted records are')
data = cursor.execute('SELECT * from STUDENT')
for row in data:
    print(row)
    
## commit your changes in databse
connection.commit()
connection.close()