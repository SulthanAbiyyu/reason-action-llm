from src.tools import calculator


def test_calculator():
    assert calculator("1+1") == 2
    assert calculator("1-1") == 0
    assert calculator("5*3") == 15
    assert calculator("10/2") == 5
    assert calculator("10%3") == 1
    assert calculator("2^3") == 8.0
