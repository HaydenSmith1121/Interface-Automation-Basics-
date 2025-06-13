import pytest

from comm.seafile_func import *


@pytest.fixture
def func1():
    print("上班跑外卖")
    yield 100
    print("下班按摩")


@pytest.fixture
def func2():
    print("上班跑滴滴")
    yield 200
    print("下班洗脚")


@pytest.fixture
def func3():
    print("上班送快递")
    yield 300
    print("下班打赏女主播")


@pytest.fixture
def func4():
    yield sea_file_login("seafile@admin.com", "admin").json()["token"]
