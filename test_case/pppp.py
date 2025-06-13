import testtest
from comm.sea_file_tools import sea_file_1_3

testtest.func1()

repo_id = sea_file_1_3("8ac00e05a7652b31598a56d764bd5b5f7c45a6ef", "test_repo")
print(repo_id.json()["repo_id"])