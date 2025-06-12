import pytest


@pytest.mark.xfail
def test_skip_01():
    assert 1 == 2


@pytest.mark.xfail
def test_skip_02():
    assert 1 == 1


@pytest.mark.xfail
def test_skip_03():
    assert 1 == 1
