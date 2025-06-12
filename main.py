import pytest

if __name__ == '__main__':
    # 用例文件的位置和报告文件的位置都是相对于当前main文件而言的
    pytest.main(["-sv", "test_case/test_06.py", '--html=report/my_report_05.html'])
