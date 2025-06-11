import pymysql

# 创建数据库连接对象
scott = pymysql.connect(host='192.168.79.132', port=3306,
                        user='root', password='123456',
                        db='scott', charset='utf8')

# 创建游标对象（默认是元组游标）
scott_cur = scott.cursor()
# 写sql语句
sql = "select * from emp;"
# 执行sql语句
scott_cur.execute(sql)
# 从游标对象中获取结果
result = scott_cur.fetchall()
# 关闭游标对象和数据库连接对象
scott_cur.close()
scott.close()
# 输出结果
print(result)
