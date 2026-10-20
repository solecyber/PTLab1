"""Tests for the calculation required by variant 10."""

from src.AcademicDebtCounter import AcademicDebtCounter


def test_count_students_with_exactly_two_debts() -> None:
    data = {
        "Exactly two": [("a", 60), ("b", 0), ("c", 61)],
        "One": [("a", 60), ("b", 61), ("c", 100)],
        "Three": [("a", 60), ("b", 50), ("c", 40)],
        "None": [("a", 61), ("b", 80)],
    }

    counter = AcademicDebtCounter(data)

    assert counter.student_names() == ["Exactly two"]
    assert counter.count() == 1


def test_count_returns_zero_for_empty_data() -> None:
    counter = AcademicDebtCounter({})

    assert counter.student_names() == []
    assert counter.count() == 0
