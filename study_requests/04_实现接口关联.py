from comm.seafile_func import *

r = sea_file_login("seafile@admin.com", "admin")
print("_" * 50)
token = eval(r.text)["token"]
r2=sea_file_get_all_info(token)
print(f"{r2.text}")
