# pip install mysql-connector-python
from mysql.connector import *
from . import get_mysql_config


def execute_sql(sql):
    """执行sql语句

    :param sql: sql语句
    :return: 查询结果
    """
    # 创建数据库连接对象
    db = connect(host=get_mysql_config.get_mysql_config()["host"],
                 port=get_mysql_config.get_mysql_config()["port"],
                 user=get_mysql_config.get_mysql_config()["user"],
                 password=get_mysql_config.get_mysql_config()["password"],
                 db=get_mysql_config.get_mysql_config()["db"],
                 charset=get_mysql_config.get_mysql_config()["charset"])

    # 创建游标
    cur = db.cursor()
    try:
        cur.execute(sql)
        # 去前后空格，并转小写
        if sql.strip().lower().startswith(('insert', 'update', 'delete')):
            db.commit()
        print("执行成功")
    # 捕获mysql相关的异常
    except Exception as e:
        db.rollback()
        print("执行失败")
    # 获取查询结果，并用一个python对象接收
    # .fetchone()获取单条数据
    # .fetchall()获取全部数据
    result = cur.fetchall()
    # 关闭游标和数据库连接
    cur.close()
    db.close()
    return result
