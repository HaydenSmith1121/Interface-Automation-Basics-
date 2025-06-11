import requests

# sea_file的地址
url = "http://192.168.79.131:38000/api2/auth-token/"

# 请求头信息
headers = {"content-type": "application/x-www-form-urlencoded"}

# 请求体信息
body = {"username": "seafile@admin.com", "password": "admin"}

# url参数对应请求地址，headers对应请求头，data对应请求体
response = requests.post(url=url, headers=headers, data=body)

print(f"响应码{response.status_code}")
print(f"响应头{response.headers}")
print(f"响应体{response.text}")
print(f"响应时间{response.elapsed.total_seconds()}")
