import pytest
from comm.seafile_func import *
from comm.tools import *

resp = sea_file_login(username='seafile@admin.com', password='admin')


# 1.断言响应头
def test_sea_file_login_headers():
    assert resp.headers.get('Content-Type') == 'application/json'


# 2.断言响应体
def test_sea_file_login_body():
    assert 'token' in resp.text


# 3.断言Json
def test_sea_file_login_json():
    token = get_str_by_re(left='"token":', right='"', str=resp.text)
    assert token == 'b8606ef5954da45961b6a2c9f7c42dbb60b71676'


# 4.断言状态码
def test_sea_file_login_status_code():
    assert 200 == resp.status_code


# 5.断言响应时间
def test_sea_file_login_elapsed_time():
    assert 200 / 1000 >= resp.elapsed.total_seconds()


resp1 = sea_file_get_all_info(token=resp.json().get('token'))


# 6.断言响应头
def test_sea_file_get_all_info_headers():
    assert resp1.headers.get('Content-Type') == 'application/json'


# 7.断言响应体
def test_sea_file_get_all_info_body():
    assert 'email' in resp1.text


# 8.断言状态码
def test_sea_file_get_all_info_status_code():
    assert resp1.status_code == 200


# 9.断言响应时间
def test_sea_file_get_all_info_elapsed_time():
    assert resp1.elapsed.total_seconds() <= 200 / 1000


if __name__ == '__main__':
    pytest.main(['-sv', '06_断言.py'])
