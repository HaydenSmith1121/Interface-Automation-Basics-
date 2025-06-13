import pytest

from comm.seafile_func import *
from comm.tools import get_csv_data

print(sea_file_login("seafile@admin.com", "admin").text)


@pytest.mark.parametrize(["username", "password", "code", "msg"], get_csv_data("./data/01seafile_login.csv"))
def test_sea_file_login(username, password, code, msg):
    response = sea_file_login(username, password)
    a = eval(code)
    assert response.status_code == a
    assert msg in response.text


@pytest.mark.parametrize(["token", "code", "msg"], get_csv_data("./data/02seafile_info.csv"))
def test_sea_file_info(token, code, msg):
    response = sea_file_get_all_info(token)
    a = eval(code)
    assert response.status_code == a
    assert msg in response.text


@pytest.mark.parametrize(["token", "repo_name", "code", "msg"], get_csv_data("./data/03seafile_add_repo.csv"))
def test_sea_file_add_repo(token, repo_name, code, msg):
    response = sea_file_add_repo(token, "test_repo")
    a = eval(code)
    assert response.status_code == a
    assert msg in response.text


rs = sea_file_add_repo('8ac00e05a7652b31598a56d764bd5b5f7c45a6ef', "name")
# print(rs.json()["repo_id"])
repo_id = rs.json()['repo_id']
response = sea_file_update_repo('8ac00e05a7652b31598a56d764bd5b5f7c45a6ef', repo_id, "aaa")
print(response.text)


#
# # "------------------------------------------------------------"
@pytest.mark.parametrize(['token', 'code', 'name', 'result'], get_csv_data("./data/05seafile_update_repo.csv"))
def test_sea_file_update_repo(token, code, name, result):
    # response = sea_file_update_repo(token, repo_id, name)
    assert response.status_code == int(code)
    assert result in response.text
