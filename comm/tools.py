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

# 正则表达式的所有方法：
#     re.match(pattern, string, flags=0)
#     re.search(pattern, string, flags=0)
#     re.findall(pattern, string, flags=0)
#     re.finditer(pattern, string, flags=0)
#     re.sub(pattern, repl, string, count=0, flags=0)
#     re.split(pattern, string, maxsplit=0, flags=0)
#     re.compile(pattern, flags=0)
#     re.purge()
#     re.error
#     re.escape(string)
#     re.IGNORECASE
#     re.DOTALL
#     re.MULTILINE
#     re.VERBOSE
#     re.DEBUG
#     re.A
#     re.L
#     re.M
#     re.S
#     re.U
#     re.X
#     re.I
#     re.X
#     re.I
#     re.X
