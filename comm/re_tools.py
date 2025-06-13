import csv
import json
import re


def get_str_by_re(left="\\A", right="\\Z", str="", flag=1):
    """
        使用正则表达式匹配左右两边的字符串，返回中间的字符串。
        默认是返回匹配结果，不包含匹配规则。
        可以通过flag参数来返回匹配结果中的第几个结果。
        设置flag=0可以获取匹配结果中的所有字符串。
    """
    result = re.search(left + "(.*?)" + right, str)
    return result.group(flag) if result else "没找到~"
