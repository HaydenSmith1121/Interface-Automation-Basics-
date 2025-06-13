# 正则表达式的语法规则
# 1. 匹配字符：
#     .  匹配任意字符
#     \d 匹配数字
#     \D 匹配非数字
#     \w 匹配字母数字下划线
#     \W 匹配非字母数字下划线
#     \s 匹配空白字符
#     \S 匹配非空白字符
#     \b 匹配单词边界
#     \B 匹配非单词边界
#     \A 匹配字符串的开头
#     \Z 匹配字符串的结尾
#     \z 匹配字符串的结尾
#     \G 匹配字符串的当前位置
#     \1 匹配第一个分组的内容
# 2. 匹配字符串：
#     ^ 匹配字符串的开头
#     $ 匹配字符串的结尾
#     | 匹配或
#     () 匹配分组
#     [ ] 匹配字符集合
#     [^ ] 匹配非字符集合
#     {n} 匹配n个字符
#     {n,} 匹配n个以上字符
#     {n,m} 匹配n到m个字符
#     * 匹配0个或多个字符
#     + 匹配1个或多个字符
#     ? 匹配0个或1个字符
#     . 匹配任意字符
# 正则表达式的使用方法
# 1. 匹配字符串：
#     re.match(pattern, string, flags=0)
#     re.search(pattern, string, flags=0)
#     re.findall(pattern, string, flags=0)
#     re.finditer(pattern, string, flags=0)
#     re.sub(pattern, repl, string, count=0, flags=0)
#     re.split(pattern, string, maxsplit=0, flags=0)
#     re.compile(pattern, flags=0)
#     re.purge()
#     re.error
#
from comm.tools import *
from comm.sea_file_tools import *

# 登录获取token
r = sea_file_1_1("seafile@admin.com", "admin")

# 使用正则表达式获取token值
token = get_str_by_re('":"', '"', f'{r.text}')
# 使用json方式获取token值
token1 = r.json()["token"]

# 获取账号信息
info = sea_file_1_2(token1)

# # 正则表达式练习
# s2 = "'Content-Length': '237', 'Content-Type': 'application/json'"
# # 使用get_str_by_re函数匹配：application/json值
# print(get_str_by_re("Type': '", "'", s2))
#
# s3 = '{"token":"8ac00e05a7652b31598a56d764bd5b5f7c45a6ef"}'
# # 使用get_str_by_re函数匹配：token值
# print(get_str_by_re('":"', '"', s3))
