import pytest

from comm.re_tools import get_json_data


@pytest.mark.parametrize(["x", "y"], get_json_data("./data/json_data.json"))
def test_json_data(x, y):
    assert x + y > 5
