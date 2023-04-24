import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='weapon'
)
# 创建游标对象
cursor = connection.cursor()
# # 执行SQL语句以创建新的表
# cursor.execute('CREATE TABLE users (id INT, name VARCHAR(255), email VARCHAR(255))')

# 执行SQL语句以查看数据库中的表
cursor.execute("SHOW TABLES")

# 获取结果
result = cursor.fetchall()

# 打印结果
for row in result:
    print(row)

cursor.close()
connection.close()