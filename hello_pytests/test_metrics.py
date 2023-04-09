"""
Unit tests checking basic functionality of commercial calculations.
"""
import metrics


def test_profit() -> None:
    """
    Test profit function for basic cases
    """
    assert metrics.profit([1, 2, 3], [1, 1, 1]) == 3


def test_margin() -> None:
    """
    Test margin function for basic cases
    """
    assert metrics.margin([1, 2, 3], [1, 1, 1]) == 0.5


def test_markup() -> None:
    """
    Test markup function for basic cases
    """
    assert metrics.markup([1, 2, 3], [1, 1, 1]) == 1.0
