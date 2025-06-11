# 详情在comm包下的seafile_func.py模块中
# 导入写好的登录函数
from comm.seafile_func import sea_file_login as l

# r = l("seafile@admin.com", "admin")
# 设置编码格式为UTF-8
# r.encoding = "utf-8"

# 用脚本实现多次调用
r1 = l("seafile@admin.com", "admin")
print("_" * 50)
r2 = l("", "admin")
print("_" * 50)
r3 = l("seafile@admin.com", "")
print("_" * 50)
r4 = l("", "")
