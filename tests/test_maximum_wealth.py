import pytest
from solutions.maximum_wealth import Solution

@pytest.mark.parametrize(
    "accounts,expected",
    [
        # Happy path: multiple customers, typical values
        ([[1, 2, 3], [3, 2, 1]], 6),
        # Happy path: single customer
        ([[10, 20, 30]], 60),
        # Happy path: multiple customers, different balances
        ([[1, 5], [7, 3], [3, 5]], 10),
        # Edge case: empty accounts list
        ([], 0),
        # Edge case: all customers have zero balances
        ([[0, 0, 0], [0, 0, 0]], 0),
        # Edge case: one customer, all zero
        ([[0, 0, 0]], 0),
        # Edge case: customer with negative balances (if allowed)
        ([[-1, -2, -3], [-4, -5, -6]], -6),
        # Edge case: mix of positive and negative balances
        ([[1, -2, 3], [4, -5, 6]], 7),
        # Edge case: single account per customer
        ([[5], [10], [3]], 10),
        # Edge case: very large numbers
        ([[10**6, 10**6], [2*10**6]], 2*10**6),
        # Edge case: customer with empty account list
        ([[], [1, 2, 3]], 6),
        # Edge case: all customers with empty account lists
        ([[], [], []], 0),
    ],
    ids=[
        "two_customers_typical",
        "single_customer",
        "three_customers_varied",
        "empty_accounts",
        "all_zero_balances",
        "one_customer_all_zero",
        "negative_balances",
        "mixed_positive_negative",
        "single_account_per_customer",
        "very_large_numbers",
        "customer_with_empty_account",
        "all_customers_empty_accounts",
    ]
)
def test_maximum_wealth_happy_and_edge_cases(accounts, expected):

    # Arrange
    solution = Solution()

    # Act
    result = solution.maximumWealth(accounts)

    # Assert
    assert result == expected

@pytest.mark.parametrize(
    "accounts,expected_exception",
    [
        # Error case: None as input
        (None, TypeError),
        # Error case: accounts is not a list
        ("not a list", TypeError),
        # Error case: account contains non-iterable
        ([1, 2, 3], TypeError),
        # Error case: account contains non-numeric values
        ([["a", "b", "c"]], TypeError),
        # Error case: account contains None
        ([[None, 1, 2]], TypeError),
    ],
    ids=[
        "input_none",
        "input_not_list",
        "account_not_iterable",
        "account_non_numeric",
        "account_contains_none",
    ]
)
def test_maximum_wealth_error_cases(accounts, expected_exception):

    # Arrange
    solution = Solution()

    # Act & Assert
    with pytest.raises(expected_exception):
        solution.maximumWealth(accounts)
