from chap07.第七章作业 import path_date
import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
)
cursor = connection.cursor()
sql0 = '''
CREATE DATABASE DATA;
'''

sql1 = '''
CREATE TABLE DATA.ID(
    id INT, 
    JG VARCHAR(255), 
    );
'''

sql2 = '''
CREATE TABLE DATA.WORDS(
    title VARCHAR(255),
)
'''

sql3 = '''
CREATE TABLE DATA.ATTRS(
    attrs VARCHAR(255)
)
'''

sql4 = '''
CREATE TABLE DATA.TIPS(
    tips VARCHAR(255)
)
'''
cursor.execute('')