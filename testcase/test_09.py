import pytest


# 对生成器进行pytest的fixture装饰之后，这个函数就 成为了fixture
@pytest.fixture(scope='function', autouse=False)
def func():
    print('开始热身运动慢跑15分钟...')
    yield 15
    print('开始进行拉伸运动5分钟...')


def test_001(func):
    print(f'热身结束，一共花了{func}分钟')
    print('现在开始撸铁')
    print('正在练习我的肱二头肌')


def test_002():
    print('现在开始撸铁')
    print('正在练习我的肱三头肌')


class TestA:
    # 类
    # 当类中第一个用例开始执行之前，会触发fixture前置
    # 当类中最后一个用例执行结束之后，会触发fixture后置
    def test_003(self,func):
        print('现在开始撸铁')
        print('正在练习我的肱四头肌')

    def test_004(self):
        print('现在开始撸铁')
        print('正在练习我的肱五头肌')
    # class TestA:
    # def test_005(self):
    # print('我是测试用例005号')
    # print('我正在执行005')
    # print('我执行结束啦005')
