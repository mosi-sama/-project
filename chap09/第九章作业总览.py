# encoding:utf-8
import pymysql

path = '整合的数据.txt'

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
)

cursor = connection.cursor()