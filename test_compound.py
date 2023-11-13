from src.looping import compound_interest


def test_compound_interest():
    def expected_compound_interest(pv, ir, yr, n):
        future_value = pv * (1 + ir) ** n
        if (ir == 0):
            future_value += yr * n
        else:
            future_value += yr * (((1 + ir) ** n - 1) / ir)
        return future_value

    assert compound_interest(0, 0, 0, 0) == 0, "Test Failed: Expected 0"
    assert round(compound_interest(0, 0.05, 100, 5), 2) == round(
        expected_compound_interest(0, 0.05, 100, 5), 2
    ), "Test Failed: Expected 552.56"
    assert compound_interest(1000, 0, 100, 5) == expected_compound_interest(
        1000, 0, 100, 5
    ), "Test Failed: Expected 1500"
    assert round(compound_interest(1000, 0.05, 0, 5), 2) == round(
        expected_compound_interest(1000, 0.05, 0, 5), 2
    ), "Test Failed: Expected 1276.28"
    assert round(compound_interest(1000, 0.05, 100, 5), 2) == round(
        expected_compound_interest(1000, 0.05, 100, 5), 2
    ), f"Test Failed: Expect {expected_compound_interest(1000, 0.05, 100, 5)}"
    assert round(compound_interest(-1000, 0.05, 100, 5), 2) == round(
        expected_compound_interest(-1000, 0.05, 100, 5), 2
    ), f"Test Failed: Expect {expected_compound_interest(-1000, 0.05, 100, 5)}"
    assert round(compound_interest(1000, -0.05, 100, 5), 2) == round(
        expected_compound_interest(1000, -0.05, 100, 5), 2
    ), f"Test Failed: Expect {expected_compound_interest(1000, -0.05, 100, 5)}"
