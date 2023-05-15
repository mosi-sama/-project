# encoding:utf-8
from chap09.第九章作业总览 import cursor, connection

sql1 = '''
CREATE TABLE DATA.info(
    id INT, 
    JG VARCHAR(255), 
    title VARCHAR(255),
    attrs VARCHAR(255),
    tips VARCHAR(255)
    );
'''

cursor.execute(sql1)

connection.commit()

cursor.close()

connection.close()