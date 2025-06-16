from mysql_tools.mysql_tools import *

sql = 'select * from emp'

result = execute_sql(sql)

# print(result)
for i in result:
    print(i)
