import pytest


@pytest.mark.skip
def test_skip_01():
    assert 1 == 2


@pytest.mark.skipif(1 < 2, reason="skip if 1<2")
def test_skip_02():
    assert 1 == 1


@pytest.mark.skipif(1 > 2, reason="skip if 1>2")
def test_skip_03():
    assert 1 == 1
