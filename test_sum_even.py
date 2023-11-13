from src.looping import sum_even_nums


def test_sum_even_nums():
    assert sum_even_nums(1) == 0, "Test Failed: Expected 0"
    assert sum_even_nums(2) == 2, "Test Failed: Expected 2"
    assert sum_even_nums(3) == 2, "Test Failed: Expected 2"
    assert sum_even_nums(4) == 6, "Test Failed: Expected 6"
    assert sum_even_nums(10) == 30, "Test Failed: Expected 30"
    assert sum_even_nums(100) == 2550, "Test Failed: Expected 2550"
