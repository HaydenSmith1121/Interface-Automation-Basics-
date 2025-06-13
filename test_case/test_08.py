# fixture夹具
import pytest



@pytest.fixture
def func():
    print("用例执行之前")
    yield 300
    print("用例执行之后")


def test_case1(func):
    print("用例1执行")
    print(f"{func}")
