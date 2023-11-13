from src.looping import sum_nums


def test_sum_nums():
    assert sum_nums(1) == 1, "Test Failed: Expected 1"
    assert sum_nums(2) == 3, "Test Failed: Expected 3"
    assert sum_nums(3) == 6, "Test Failed: Expected 6"
    assert sum_nums(4) == 10, "Test Failed: Expected 10"
    assert sum_nums(10) == 55, "Test Failed: Expected 55"
    assert sum_nums(100) == 5050, "Test Failed: Expected 5050"
