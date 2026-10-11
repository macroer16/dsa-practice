# Algorithms and data structures practice

[![Tests](https://github.com/macroer16/dsa-practice/actions/workflows/tests.yml/badge.svg)](https://github.com/macroer16/dsa-practice/actions/workflows/tests.yml)

My practice for coding interviews and online assessments (like HackerRank), in Python. Every solution here is my own. Each one is tested, and each file explains my approach and its time and space complexity in my own words.

## Progress

<!-- progress:start -->
**0 of 10 solved**

| Problem | Topic | Pattern | Difficulty | My solution | Status |
|---|---|---|---|---|---|
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Arrays hashing | Hash set | Easy | [code](problems/arrays_hashing/contains_duplicate.py) | ⬜ Not started |
| [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays hashing | Hash map of values seen so far | Easy | [code](problems/arrays_hashing/two_sum.py) | ⬜ Not started |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Arrays hashing | Counting with a hash map | Easy | [code](problems/arrays_hashing/valid_anagram.py) | ⬜ Not started |
| [Binary Search](https://leetcode.com/problems/binary-search/) | Binary search | Binary search | Easy | [code](problems/binary_search/binary_search.py) | ⬜ Not started |
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Dynamic programming | Dynamic programming (it's Fibonacci in disguise) | Easy | [code](problems/dynamic_programming/climbing_stairs.py) | ⬜ Not started |
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Dynamic programming | Kadane's algorithm | Medium | [code](problems/dynamic_programming/maximum_subarray.py) | ⬜ Not started |
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked list | Pointer reversal | Easy | [code](problems/linked_list/reverse_linked_list.py) | ⬜ Not started |
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Sliding window | Track the lowest price so far | Easy | [code](problems/sliding_window/best_time_to_buy_sell.py) | ⬜ Not started |
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | Stack | Easy | [code](problems/stack/valid_parentheses.py) | ⬜ Not started |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two pointers | Two pointers from both ends | Easy | [code](problems/two_pointers/valid_palindrome.py) | ⬜ Not started |
<!-- progress:end -->

## How I practise

1. **Read the problem** on its link and in the summary at the top of the file.
2. **Try it for 25 minutes** without looking anything up. Write the idea in plain English first, then the code.
3. **Run the tests:** `pytest -k two_sum` (or any problem name).
4. If I'm stuck, **look at the pattern name** in the file, then a hint, and only then a solution. If I needed a solution, I come back and redo it from scratch two days later.
5. **Fill in the notes:** my approach, Big-O time and space, and what I learned.
6. **Update the table:** `python tools/progress.py`, then commit.

Target: **3 to 5 problems a week**, around coursework.

## Running it

```bash
pip install -r requirements-dev.txt
pytest                      # unsolved problems are skipped, not failed
pytest -k climb_stairs      # just one problem
python tools/progress.py    # refresh the progress table above
```

## Structure

```
problems/
  arrays_hashing/    hash sets and maps
  two_pointers/      pointers moving in from both ends
  sliding_window/    tracking the best value as you scan
  stack/             last in, first out
  binary_search/     halving a sorted search space
  linked_list/       pointer manipulation (node.py has the ListNode class)
  dynamic_programming/  reusing answers to smaller problems
tests/               tests with normal and edge cases for every problem
tools/progress.py    builds the progress table from the test results
```

## Adding a new problem

1. Copy any problem file and change the docstring (title, link, difficulty, pattern, my own summary).
2. Add tests to `tests/test_problems.py`, including the edge cases: empty input, one item, negatives and duplicates.
3. Run `python tools/progress.py` and the new problem appears in the table.

## Roadmap

- **Now:** these 10 starters, one for each core pattern.
- **Next:** the [Grind 75](https://www.techinterviewhandbook.org/grind75) list, in its suggested order.
- **Later:** [NeetCode 150](https://neetcode.io/practice), grouped by the same patterns.

Problem summaries are written in my own words, with links to the original problems.
