import requests

# 百度的域名(地址)
url = "https://www.baidu.com"

# 使用Requests模块发送GET请求
response = requests.get(url)
# 设置响应内容的编码格式为UTF-8
response.encoding = "utf-8"

# 输出响应码
print(f"响应码{response.status_code}")

# 输出响应头
print(f"响应头{response.headers}")

# 输出响应体
print(f"响应体{response.text}")
print(f"响应体{response.content}")

# 输出响应时间
print(f"响应时间{response.elapsed}")
#
# # 将二进制转换为utf-8
# print(requests.get(url).content.decode("utf-8"))

