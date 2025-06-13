import pytest

from comm.sea_file_tools import *
from comm.tools import get_csv_data


@pytest.mark.parametrize(["username", "password"], get_csv_data("data/seafile_login_data.csv"))
def test_sea_file_login(username, password):
    response = sea_file_1_1(username, password)
    assert response.status_code == 200
