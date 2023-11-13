from src.looping import sum_odd_nums


def test_sum_odd_nums():
    assert sum_odd_nums(1) == 1, "Test Failed: Expected 1"
    assert sum_odd_nums(2) == 1, "Test Failed: Expected 1"
    assert sum_odd_nums(3) == 4, "Test Failed: Expected 4"
    assert sum_odd_nums(4) == 4, "Test Failed: Expected 4"
    assert sum_odd_nums(10) == 25, "Test Failed: Expected 25"
    assert sum_odd_nums(100) == 2500, "Test Failed: Expected 2500"
