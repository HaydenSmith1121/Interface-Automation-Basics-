import configparser
import os.path


def get_mysql_config():
    # 创建configparser对象,用来读取配置文件
    config = configparser.ConfigParser()

    # 配置文件的路径
    mysql_config_path = os.path.dirname(__file__) + "\\mysql_config.ini"

    # 读取ini文件
    config.read(mysql_config_path, encoding="utf-8")

    # 获取mysql配置项
    mysql_config = {
        "host": config.get("mysql", "host"),
        "port": config.get("mysql", "port"),
        "user": config.get("mysql", "user"),
        "password": config.get("mysql", "password"),
        "db": config.get("mysql", "db"),
        "charset": config.get("mysql", "charset")
    }

    return mysql_config
