"""
Looping Practice Module
=======================

This module contains a set of functions designed to provide practice
with Python's looping mechanisms. These functions cover various common
tasks that can be solved using loops, such as summing numbers,
calculating Net Present Value (NPV), and determining monthly mortgage payments.

Functions:
----------
- `sum_nums(number: int) -> int`:
    Calculates the sum of all numbers from 1 up to and including
    the given number.

- `sum_even_nums(number: int) -> int`:
    Calculates the sum of all even numbers from 1 up to and
    including the given number.

- `sum_odd_nums(number: int) -> int`:
    Calculates the sum of all odd numbers from 1 up to and
    including the given number.

- `NPV(pv: float, ir: float, n: int, pmt: float) -> float`:
    Calculates the Net Present Value (NPV) for an investment.

- `mortgage_payment(iv: float, ir: float, n: int) -> float`:
    Calculates the monthly mortgage payment for a given initial value,
    interest rate, and number of periods.

Note:
-----
All functions in this module are meant to be solved using explicit loops,
not using list comprehensions, sum(), or other built-in Python functions
for calculations.

"""


def sum_nums(number):
    """
    Calculates the sum of all numbers from 1 up to and
    including the given number.

    Parameters:
        number (int): The number up to which the sum should be calculated.

    Returns:
        int: The sum of all numbers from 1 to `number`.

    Note:
        Use explicit looping for this task. Do not use
        list comprehensions, sum(), or other built-in Python functions.
    """
    # Store number to calculate the sum of all numbers up to that 'number' and
    #  the initial value for the sum as 's'
    s = 0
    # Run loop 'number' amount of times and stop at 'number + 1' since the
    # range won't add the stop number but we want it included
    for i in range(1, number + 1, 1):
        s += i
    print("Sum is:", s)
    return number


def sum_even_nums(number):
    """
    Calculates the sum of all even numbers from 1 up to and
    including the given number.

    Parameters:
        number (int): The number up to which the sum of even numbers
        should be calculated.

    Returns:
        int: The sum of all even numbers from 1 to `number`.

    Note:
        Use explicit looping for this task. Do not use
        list comprehensions, sum(), or other built-in Python functions.
    """
    # Store number to calculate the sum of even numbers, up to that number
    #  and the initial value for the sum as 's'
    s = 0
    # Run loop 'number' amount of times and stop at 'number + 1' since the
    # range won't add the stop number but we want it included
    for i in range(0, number + 1, 2):
        s += i
    print("Sum is:", s)
    return number


def sum_odd_nums(number):
    """
    Calculates the sum of all odd numbers from 1 up to and
    including the given number.

    Parameters:
        number (int): The number up to which the sum of odd numbers
        should be calculated.

    Returns:
        int: The sum of all odd numbers from 1 to `number`.

    Note:
        Use explicit looping for this task. Do not use
        list comprehensions, sum(), or other built-in Python functions.
    """
    # Store number to calculate the sum of odd numbers, up to that number
    #  and the initial value for the sum as 's'
    s = 0

    # Run loop 'number' amount of times and stop at 'number + 1' since the
    # range won't add the stop number but we want it included
    for i in range(1, number + 1, 2):
        s += i
    print("Sum is:", s)
    return number

def compound_interest(
    initial_value, interest_rate, yearly_contribution, num_years
):
    """
    Calculates the future value of an investment with compound interest
    and yearly contributions.
    Parameters:
        initial_value (float): The initial amount of money invested.
        interest_rate (float): The annual interest rate as a decimal.
        For example, for a 5% interest rate, the value would be 0.05.
        yearly_contribution (float): The amount of money added to the
        investment each year.
        num_years (int): The number of years the money is invested for.
    Returns:
        float: The future value of the investment after `num_years`, accounting
            for compound interest and yearly contributions.
    Note:
        This function assumes that the interest is compounded annually and that
        yearly contributions are made at the end of each year.
    """
    for year in range(1, num_years + 1):
            initial_value = initial_value * (1 + interest_rate/yearly_contribution) ** num_years
            initial_value += yearly_contribution
    return initial_value

def mortgage_payment(initial_value, interest_rate, amortization):
    """
    Calculates the monthly mortgage payment for a given initial value,
    interest rate, and amortization period. If the amortization is
    <= 0, this function returns 0.

    Parameters:
        initial_value (float): The initial value or principal
            amount of the mortgage.
        interest_rate (float): The monthly interest rate as a decimal.
            For example, for a 5% annual interest rate, the monthly rate
            would be 0.05/12.
        amortization (int): The total number of years over which the
            mortgage will be repaid (loan term).

    Returns:
        float: The monthly mortgage payment or 0 if amortization <= 0.

    Note:
        Use explicit looping for this task. Do not use list comprehensions or
        other built-in Python functions for calculating the mortgage payment.
    """
    for month in range(1, amortization * 12 + 1):
        try:
            monthly_payment = (initial_value * (interest_rate / 12)) / (
                1 - (1 + interest_rate / 12) ** -month)
        except ValueError:
            if amortization <= 0:
                return 0
    return monthly_payment


if __name__ == "__main__":
    # You can do additional tests here.
    while True:
        try:
            sum_nums(int(input("Sum of ALL numbers from 1 to: ")))
            break
        except ValueError:
            print("Invalid input. Enter an integer.")
    while True:
        try:
            sum_even_nums(int(input("Sum of EVEN numbers from 1 to: ")))
            break
        except ValueError:
            print("Invalid input. Enter an integer.")
    while True:
        try:
            sum_odd_nums(int(input("Sum of ODD numbers from 1 to: ")))
            break
        except ValueError:
            print("Invalid input. Enter an integer.")

        # Approximate difference in mortgage costs over the past ~4 years
    print(mortgage_payment(300000, 0.02, 25))  # Should be ~$1271/mth
    print(mortgage_payment(450000, 0.07, 25))  # Should be ~$3160/mth!
    
    print(compound_interest(1500, 0.05, 100, 5))