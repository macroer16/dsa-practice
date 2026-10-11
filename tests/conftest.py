"""Shared test helper: unsolved problems are skipped instead of failing.

A problem counts as unsolved while its function still raises NotImplementedError,
so the test suite (and GitHub Actions) stays green while you work through the list.
"""
import pytest


def attempt(fn, *args):
    """Call a solution; skip the test if it hasn't been written yet."""
    try:
        return fn(*args)
    except NotImplementedError:
        pytest.skip(f"{fn.__name__} not solved yet")
