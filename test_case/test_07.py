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
