from comm.sea_file_tools import *

r = sea_file_1_3("8ac00e05a7652b31598a56d764bd5b5f7c45a6ef", "test_repo")
print(r.text)
print(r.json()["repo_id"])