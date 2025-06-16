# pip install mysql-connector-python
from mysql.connector import *
from . import get_mysql_config


def execute_sql(sql):
    """执行sql语句

    :param sql: sql语句
    :return: 查询结果
    """

    db = None
    cur = None
    try:
        config = get_mysql_config.get_mysql_config()
        # 创建数据库连接对象
        db = connect(host=config["host"],
                     port=int(config["port"]),
                     user=config["user"],
                     password=config["password"],
                     db=config["db"],
                     charset=config["charset"])

        # 创建游标
        cur = db.cursor()
        cur.execute(sql)
        # 去前后空格，并转小写
        if sql.strip().lower().startswith(('insert', 'update', 'delete')):
            db.commit()
        print("执行成功")
        return cur.fetchall()
    # 捕获mysql相关的异常
    except Exception as e:
        if db is not None:
            db.rollback()
        print(f"执行失败，错误信息：{str(e)}")
        return None
    finally:
        # 关闭游标和数据库连接
        if cur is not None:
            cur.close()
        if db is not None:
            db.close()
