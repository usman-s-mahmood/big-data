from flask import Flask
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='flask_test'
)
cursor = conn.cursor()
q1 = '''
    create table users (
        id int primary key auto_increment,
        first_name varchar(50) not null,
        last_name varchar(50) not null,
        username varchar(250) not null unique,
        email varchar(250) not null unique
    );
'''
cursor.execute(
    'desc users;'
)

q2 = '''
    insert into users (
        first_name, last_name,
        username, email
    ) values (
        'user', 'name',
        'username', 'user@mail.com'
    );
'''
# cursor.execute(q2)
q3 = '''select * from flask_test.users;'''
# cursor.execute(q3)
# table = cursor.fetchall()

if __name__ == '__main__':
    if conn.is_connected:
        print('connection made!')
    else:
        print('No Connection found')
    # print('\n Table Data:') 
    # for row in table: 
    #     print(row[0], end=" ") 
    #     print(row[1], end="\n") 
