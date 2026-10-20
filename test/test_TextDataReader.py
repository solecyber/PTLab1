"""Tests for the text data reader."""

from pathlib import Path

import pytest

from src.TextDataReader import TextDataReader


def test_read_parses_text_file(tmp_path: Path) -> None:
    path = tmp_path / "students.txt"
    path.write_text(
        "Иванов Иван Иванович\n"
        "    математика:91\n"
        "    химия:100\n"
        "Петров Петр Семенович\n"
        "    русский язык:87\n",
        encoding="utf-8",
    )

    assert TextDataReader().read(str(path)) == {
        "Иванов Иван Иванович": [
            ("математика", 91),
            ("химия", 100),
        ],
        "Петров Петр Семенович": [("русский язык", 87)],
    }


@pytest.mark.parametrize(
    "content",
    [
        "    математика:91\n",
        "Иванов Иван Иванович\n    математика:not-a-number\n",
        "Иванов Иван Иванович\n    :91\n",
        "Иванов Иван Иванович\n    математика:101\n",
    ],
)
def test_read_rejects_invalid_text(content: str, tmp_path: Path) -> None:
    path = tmp_path / "invalid.txt"
    path.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError):
        TextDataReader().read(str(path))
