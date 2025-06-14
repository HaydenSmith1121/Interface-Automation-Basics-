# pip install mysql-connector-python
import mysql.connector as mysql


class MysqlTools:
    """连接mysql数据库

    :param host:主机ip地址
    :param port:端口号
    :param user:mysql用户名
    :param password:mysql密码
    :param db:要连接的数据库名称

    用之前先给类属性sql赋值
    """
    sql = ""

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def connect_mysql(self):
        # 创建数据库连接对象
        db = mysql.connect(host=self.host, port=self.port,
                           user=self.user,
                           password=self.password,
                           db=self.db)

        # 创建游标
        cur = db.cursor()

        # 执行查询
        try:
            cur.execute(self.sql)
            # 去前后空格，并转小写
            if self.sql.strip().lower().startswith(('insert', 'update', 'delete')):
                db.commit()
            print("执行成功")
        # 捕获mysql相关的异常
        except mysql:
            db.rollback()
            print("执行失败")
        # 获取查询结果，并用一个python对象接收
        # .fetchone()获取单条数据
        # .fetchall()获取全部数据
        result = cur.fetchall()

        # 关闭游标和数据库连接
        cur.close()
        db.close()

        # 返回查询结果
        return result
