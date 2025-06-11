import logging


class Logutil:
    def __init__(self):
        # 获取名为坤坤的日志记录器对象
        self.logger = logging.getLogger("坤坤")
        # 设置日志记录器的记录级别，大于等于INFO级别的日志才会被记录
        self.logger.setLevel(logging.INFO)
        # 创建一个streamHandler对象， 用于输出日志到控制台
        sh = logging.StreamHandler()
        # 设置输出到控制台的日志级别
        sh.setLevel(logging.INFO)
        # 设置输出到控制台的日志格式
        sh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        # 创建一个FileHandler对象， 用于输出日志到文件
        fh = logging.FileHandler("zzc.log", "a", encoding="utf-8")

        fh.setLevel(logging.WARNING)
        # 关闭文件句柄fh，释放系统资源并确保数据写入磁盘
        fh.close()
        # 将处理器sh添加到日志记录器self.logger中
        self.logger.addHandler(sh)
        # 将处理器fh添加到日志记录器self.logger中
        self.logger.addHandler(fh)

    def log(self):
        return self.logger
