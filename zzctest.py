from mysql_tools.mysql_tools import *

sql = "select * from login order by '编号' asc;"

result = execute_sql(sql)

for i in result:
    print(i)
