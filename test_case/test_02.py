import pytest

from comm.seafile_func import *


class TestSeaFileCases:
    response1 = None
    response2 = None
    response3 = None
    response4 = None
    response5 = None
    response6 = None
    response7 = None
    response8 = None
    token = None
    repo_id = None

    @classmethod
    def setup_class(cls):
        # 1.1获取登录的响应对象
        cls.response1 = sea_file_login("seafile@admin.com", "admin")
        # 获取登录的token
        cls.token = cls.response1.json()["token"]
        # 1.2获取响应的用户信息对象
        cls.response2 = sea_file_get_all_info(cls.token)
        # 1.3获取新增资料库响应对象
        cls.response3 = sea_file_add_repo(cls.token, "test_repo")
        # 获取最新的资料库id
        cls.repo_id = sea_file_get_all_repo(cls.token).json()[0]["id"]
        # 1.4获取所有资料库的响应对象
        cls.response4 = sea_file_get_all_repo(cls.token)
        # 1.5获取修改资料库的响应对象
        cls.response5 = sea_file_update_repo(cls.token, cls.repo_id, "new_test_repo")
        # # 1.6获取删除资料库的响应对象
        # cls.response6 = sea_file_delete_repo(cls.token, cls.repo_id)
        # 1.7获取新建文件响应对象
        cls.response7 = sea_file_add_file(cls.token, cls.repo_id, "test.txt")
        # # 1.8获取删除文件响应对象
        # cls.response8 = sea_file_get_all_info(cls.token)
        # 每一个类执行只运行一次
        print('类中第一个方法用例执行之前会运行内容')

    # 用例执行之前内容：每一个用例执行之前都会运行代码
    @staticmethod
    def setup_method():
        print('开始去上班.......')

    # 用例执行之后内容：每一个用例执行之后都会运行代码
    @staticmethod
    def teardown_method():
        print('现在下班啦')
        print('洗个脚，按个摩')

    @staticmethod
    def teardown_class():
        print('类中最后一个方法用例执行之后会运行内容')

    # 1.1断言登录的响应码
    def test_sea_file_login_status_code(self):
        assert self.response1.status_code == 200

    # 1.1断言登录的响应时间
    def test_sea_file_login_elapsed_time(self):
        assert self.response1.elapsed.total_seconds() < 200 / 1000

    # 1.1断言登录的响应头
    def test_sea_file_login_headers(self):
        assert self.response1.headers["Content-Type"] == "application/json"

    # 1.1断言登录的响应体
    def test_sea_file_login_body(self):
        assert "token" in self.response1.text

    # 1.2断言获取用户信息的响应码
    def test_sea_file_get_all_info_status_code(self):
        assert self.response2.status_code == 200

    # 1.2断言获取用户信息的响应时间
    def test_sea_file_get_all_info_elapsed_time(self):
        assert self.response2.elapsed.total_seconds() < 200 / 1000

    # 1.2断言获取用户信息的响应头
    def test_sea_file_get_all_info_headers(self):
        assert self.response2.headers["Content-Type"] == "application/json"

    # 1.2断言获取用户信息的响应体
    def test_sea_file_get_all_info_body(self):
        assert "email" in self.response2.text

    # 1.3断言新增资料库的响应码
    def test_sea_file_add_repo(self):
        assert self.response3.status_code == 200

    # 1.3断言新增资料库的响应时间
    def test_sea_file_add_repo_elapsed_time(self):
        assert self.response3.elapsed.total_seconds() <= 200 / 1000

    # 1.3断言新增资料库的响应头
    def test_sea_file_add_repo_headers(self):
        assert self.response3.headers["Content-Type"] == "application/json"

    # 1.3断言新增资料库的响应体
    def test_sea_file_add_repo_body(self):
        print(self.response3.text)
        assert "email" in self.response3.text

    # 1.7断言添加文件的响应码
    def test_sea_file_add_file(self):
        assert self.response7.status_code == 200

    # 1.7断言添加文件的响应时间
    def test_sea_file_add_file_elapsed_time(self):
        assert self.response7.elapsed.total_seconds() < 200 / 1000

    # 1.7断言添加文件的响应头
    def test_sea_file_add_file_headers(self):
        assert self.response7.headers["Content-Type"] == "application/json; charset=utf-8"

    # 1.7断言添加文件的响应体
    def test_sea_file_add_file_body(self):
        assert "modifier_email" in self.response7.text
