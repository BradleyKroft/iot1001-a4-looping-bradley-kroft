from src.looping import mortgage_payment


def within_margin(calculated, expected, margin=0.02, absolute_margin=2):
    absolute_margin = max(absolute_margin, expected * margin)
    lower_bound = expected - absolute_margin
    upper_bound = expected + absolute_margin
    return lower_bound <= calculated <= upper_bound


def test_mortgage_payment():
    def payment_amt(iv, ir, n):
        if n != 0:
            return (iv * (ir * (1 + ir) ** n) / ((1 + ir) ** n - 1)) / 12
        else:
            return 0

    assert mortgage_payment(0, 0, 0) == 0, "Test Failed: Expected 0"
    assert mortgage_payment(0, 0.05, 10) == 0, "Test Failed: Expected 0"
    assert (
        round(mortgage_payment(1000, 0, 5), 2) == 16.67
    ), "Test Failed: Expected 16.67"
    assert mortgage_payment(1000, 0.05, 0) == 0, "Test Failed: Expected 0"

    iv, ir, n = 1028, 0.05, 5
    expected_pmt = payment_amt(iv, ir, n)
    assert within_margin(
        mortgage_payment(iv, ir, n), expected_pmt
    ), f"Test Failed: Expected {expected_pmt}"

    iv, ir, n = 500000, 0.01, 25
    expected_pmt = payment_amt(iv, ir, n)
    assert within_margin(
        mortgage_payment(iv, ir, n), expected_pmt
    ), f"Test Failed: Expected {expected_pmt}"

    iv, ir, n = 750000, 0.07, 25
    expected_pmt = payment_amt(iv, ir, n)
    assert within_margin(
        mortgage_payment(iv, ir, n), expected_pmt
    ), f"Test Failed: Expected {expected_pmt}"

    iv, ir, n = -1000, 0.05, 3
    expected_pmt = payment_amt(iv, ir, n)
    assert within_margin(
        mortgage_payment(iv, ir, n), expected_pmt
    ), f"Test Failed: Expected {expected_pmt}"

    iv, ir, n = 1000, -0.05, 3
    expected_pmt = payment_amt(iv, ir, n)
    assert within_margin(
        mortgage_payment(iv, ir, n), expected_pmt
    ), f"Test Failed: Expected {expected_pmt}"
