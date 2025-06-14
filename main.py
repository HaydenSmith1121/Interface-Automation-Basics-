# import pytest
#
# if __name__ == '__main__':
#     pytest.main(["-sv", "testcase/test07.py", '--html=report/my_report_07.html'])
#
import os
import pytest

# 项目程序主入口
# pytest.main()
# pytest.main(['-vs', r'D:\pythonProject127\testcases\test_a.py'])
pytest.main(['-sv', './testcase/test07.py', '--clean-alluredir', '--alluredir', './allure_result'])
# 清理旧的测试报告，将allure的测试结果分析生成HTML报告
os.system('allure generate ./allure_result -o ./report --clean')
