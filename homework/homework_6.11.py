# 6.10作业
from comm.sea_file_tools import *

# 1.1登录接口
response1 = sea_file_1_1("seafile@admin.com", "admin")
print(response1)

# 获取token
token = response1.json()["token"]
print(token)

# 1.2获取用户信息
response2 = sea_file_1_2(token)
print(response2)

# 1.3新增资料库
response3 = sea_file_1_3(token, "test_repo2")
print(response3)

# 1.4查询所有资料库
response4 = sea_file_1_4(token)
print(response4)

# 获取新增的资料库的id
repo_id = response4.json()[0]["id"]
print(repo_id)

# # 1.5修改资料库的名字
response5 = sea_file_1_5(token, repo_id, "new_test_repo2")
print(response5)

# 1.6删除指定的资料库接口
response6 = sea_file_1_6(token, repo_id)
print(response6)

# 1.7在指定的资料库目录新建文件
response7 = sea_file_1_7(token, repo_id, "file.txt")
print(response7)

# 1.8在指定的资料库目录删除文件接口
response8 = sea_file_1_8(token, repo_id, "file.txt")
print(response8)

