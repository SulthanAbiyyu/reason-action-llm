from src import calculator

def test_calculator():
    assert calculator("1+1") == 2
    assert calculator("1-1") == 0
    assert calculator("5*3") == 15
    assert calculator("10/2") == 5
    assert calculator("1000 - 1000 * 10 / 100") == 900.0
    assert calculator("3 + 5 * 3") == 18.0
