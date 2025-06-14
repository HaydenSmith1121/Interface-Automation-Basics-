import allure
import pytest

from comm.sea_file_tools import *
from comm.get_data_tools import *
from comm.write_data_tools import write_data_to_csv


@allure.step("接口1（登录接口）的用例")
@pytest.mark.parametrize(["username", "password", "code", "msg"], get_csv_data("./data/01seafile.csv"))
def test_sea_file_login(username, password, code, msg):
    allure.attach("登录", "步骤01")
    response = sea_file_1_1(username, password)
    allure.attach("将输入的csv里面的code类型从str转化成int", "步骤02")
    a = eval(code)
    allure.attach("断言状态码是否符合预期", "步骤03")
    assert response.status_code == a
    allure.attach("断言响应体是否符合预期", "步骤04")
    assert msg in response.text


@allure.step("接口2（获取用户信息接口）的用例")
@pytest.mark.parametrize(["token", "code", "msg"], get_csv_data("./data/02seafile.csv"))
def test_sea_file_info(token, code, msg):
    allure.attach("获取token值", "步骤01")
    response = sea_file_1_2(token)
    allure.attach("将输入的csv里面的code类型从str转化成int", "步骤02")
    a = eval(code)
    allure.attach("断言状态码是否符合预期", "步骤03")
    assert response.status_code == a
    allure.attach("断言响应体是否符合预期", "步骤04")
    assert msg in response.text


@pytest.mark.parametrize(["token", "repo_name", "code", "msg"], get_csv_data("./data/03seafile.csv"))
def test_sea_file_add_repo(token, repo_name, code, msg):
    response = sea_file_1_3(token, "test_repo")
    a = eval(code)
    assert response.status_code == a
    assert msg in response.text


@pytest.mark.parametrize(["token", "code", "msg"], get_csv_data("./data/04seafile.csv"))
def test_sea_file_get_repo_info(token, code, msg):
    response = sea_file_1_4(token)
    a = eval(code)
    assert response.status_code == a
    assert msg in response.text


# 获取token
token_1 = sea_file_1_1("seafile@admin.com", "admin").json()["token"]
# 获取repo_id
repo_id_1 = sea_file_1_3(token_1, "test_repo").json()["repo_id"]

# 向csv文件中写入数据
data = [[token_1, repo_id_1, "test130_new", "200", "success"],
        [token_1, repo_id_1,
         "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111255",
         "200", "success"],
        [token_1, repo_id_1, "", "200", "success"],
        [token_1 + "1", repo_id_1, "1", "200", "success"],
        [token_1 + "1", repo_id_1,
         "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111255",
         "200", "success"],
        [token_1 + "1", repo_id_1, "", "200", "success"]
        ]
write_data_to_csv("./data/05seafile.csv", data, "w")


@pytest.mark.parametrize(["token", "repo_id", "repo_name", "code", "msg"], get_csv_data("./data/05seafile.csv"))
def test_sea_file_1_5(token, repo_id, repo_name, code, msg):
    response = sea_file_1_5(token, repo_id, repo_name)
    a = eval(code)
    assert response.status_code == a
    assert msg in response.text
