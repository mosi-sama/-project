import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='weapon'
)
cursor = connection.cursor()
