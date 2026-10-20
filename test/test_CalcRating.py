"""Tests for average rating calculation."""

import pytest

from src.CalcRating import CalcRating


def test_calc_returns_average_for_each_student() -> None:
    data = {
        "Абрамов Петр Сергеевич": [
            ("математика", 80),
            ("русский язык", 76),
            ("программирование", 100),
        ],
        "Петров Игорь Владимирович": [
            ("математика", 61),
            ("русский язык", 80),
            ("программирование", 78),
            ("литература", 97),
        ],
    }

    ratings = CalcRating(data).calc()

    assert ratings["Абрамов Петр Сергеевич"] == pytest.approx(85.3333)
    assert ratings["Петров Игорь Владимирович"] == pytest.approx(79.0)


def test_calc_rejects_student_without_grades() -> None:
    with pytest.raises(ValueError, match="Student has no grades"):
        CalcRating({"Иванов Иван Иванович": []}).calc()
