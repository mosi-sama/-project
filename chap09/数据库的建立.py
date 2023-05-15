# encoding:utf-8
from chap09.第九章作业总览 import cursor, connection

sql0 = '''
CREATE DATABASE DATA;
'''

cursor.execute(sql0)

cursor.close()

connection.close()