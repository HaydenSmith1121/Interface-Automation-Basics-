"""
    封装日志相关的工具
"""

import logging
import colorlog


def log_distribution(logger_name: str):
    """
    记录日志 分发日志

    :param logger_name: 日志记录器的名字，也是日志文件的名字.
    """
    # 日志记录器对象
    logger = logging.getLogger(logger_name)
    # 设置日志记录的级别
    logger.setLevel(logging.INFO)

    # 操作日志输入到控制台的对象
    console_handler = colorlog.StreamHandler()
    # 控制台输出的日志的级别
    console_handler.setLevel(logging.INFO)
    # 控制台输出的日志的格式和颜色
    formatter = colorlog.ColoredFormatter(("%(log_color)s[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"),
                                          log_colors={
                                              'DEBUG': 'cyan',
                                              'INFO': 'green',
                                              'WARNING': 'yellow',
                                              'ERROR': 'red',
                                              'CRITICAL': 'bold_red',
                                          })
    console_handler.setFormatter(formatter)

    # 操作日志输入到文件的对象
    file_handler = logging.FileHandler(logger_name, "a", encoding="utf-8")
    # 输入到文件的日志的级别
    file_handler.setLevel(logging.INFO)
    # 输入到文件的日志的格式
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # 将操作控制台和文件的日志记录器对象添加到日志记录器对象中
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # 关闭文件日志记录器对象
    file_handler.close()

    # 返回日志记录器对象
    return logger
