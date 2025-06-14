mysql = MysqlTools('192.168.79.132', 3306,
                   'root', '123456',
                   'scott')

mysql.sql = "select * from emp"

result = mysql.connect_mysql()
