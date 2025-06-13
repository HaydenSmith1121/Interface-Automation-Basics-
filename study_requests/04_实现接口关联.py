from comm.sea_file_tools import *

r = sea_file_1_1("seafile@admin.com", "admin")
print("_" * 50)
token = eval(r.text)["token"]
r2=sea_file_1_2(token)
print(f"{r2.text}")
