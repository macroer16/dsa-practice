"""Tests for every problem. Each one includes the obvious cases and the edge cases
interviewers like to ask about (empty input, one item, negatives, duplicates)."""
import pytest

from conftest import attempt
from problems.arrays_hashing.contains_duplicate import contains_duplicate
from problems.arrays_hashing.valid_anagram import is_anagram
from problems.arrays_hashing.two_sum import two_sum
from problems.two_pointers.valid_palindrome import is_palindrome
from problems.sliding_window.best_time_to_buy_sell import max_profit
from problems.stack.valid_parentheses import is_valid
from problems.binary_search.binary_search import search
from problems.linked_list.reverse_linked_list import reverse_list
from problems.linked_list.node import from_list, to_list
from problems.dynamic_programming.climbing_stairs import climb_stairs
from problems.dynamic_programming.maximum_subarray import max_sub_array


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([], False),
    ([7], False),
    ([-1, -1], True),
    (list(range(100_000)) + [99_999], True),
])
def test_contains_duplicate(nums, expected):
    assert attempt(contains_duplicate, nums) is expected


@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "ab", False),
    ("aacc", "ccac", False),
    ("", "", True),
])
def test_is_anagram(s, t, expected):
    assert attempt(is_anagram, s, t) is expected


@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-3, 4, 3, 90], 0, [0, 2]),
])
def test_two_sum(nums, target, expected):
    assert sorted(attempt(two_sum, nums, target)) == expected


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("0P", False),
    ("ab_a", True),
])
def test_is_palindrome(s, expected):
    assert attempt(is_palindrome, s) is expected


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1], 0),
    ([2, 4, 1], 2),
    ([3, 2, 6, 5, 0, 3], 4),
])
def test_max_profit(prices, expected):
    assert attempt(max_profit, prices) == expected


@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("(", False),
    (")", False),
    ("", True),
])
def test_is_valid(s, expected):
    assert attempt(is_valid, s) is expected


@pytest.mark.parametrize("nums, target, expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([5], 5, 0),
    ([5], -5, -1),
    ([1, 3], 3, 1),
    (list(range(0, 2_000_000, 2)), 1_999_998, 999_999),
])
def test_search(nums, target, expected):
    assert attempt(search, nums, target) == expected


@pytest.mark.parametrize("values", [[1, 2, 3, 4, 5], [1, 2], [7], []])
def test_reverse_list(values):
    assert to_list(attempt(reverse_list, from_list(values))) == list(reversed(values))


@pytest.mark.parametrize("n, expected", [(1, 1), (2, 2), (3, 3), (5, 8), (10, 89), (45, 1836311903)])
def test_climb_stairs(n, expected):
    assert attempt(climb_stairs, n) == expected


@pytest.mark.parametrize("nums, expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-3, -1, -2], -1),
])
def test_max_sub_array(nums, expected):
    assert attempt(max_sub_array, nums) == expected
