import pytest

from comm.log_tools import *
from test_source.add import *


class TestAdd:
    @staticmethod
    def setup_class(cls):
        cls.logger = Logutil().log()

    def test_add_file_1(self):
        self.logger.info("第1条用例开始测试")
        try:
            assert Add(1, 2).add() == 3
        except:
            self.logger.error("第1条用例测试失败")
        finally:
            self.logger.info("第1条用例测试结束")

    def test_add_file_2(self):
        self.logger.info("第2条用例开始测试")
        try:
            assert Add(1, 2).add() == 4
        except:
            self.logger.error("第2条用例测试失败")
        finally:
            self.logger.info("第2条用例测试结束")


if __name__ == '__main__':
    pytest.main(["-sv", "test_01.py"])
