"""Tests for the command-line entry point."""

from pathlib import Path

import pytest

from src.main import get_path_from_arguments, main


def test_get_path_from_correct_arguments() -> None:
    assert get_path_from_arguments(["-p", "data.txt"]) == "data.txt"


def test_get_path_requires_option() -> None:
    with pytest.raises(SystemExit):
        get_path_from_arguments(["data.txt"])


def test_main_prints_ratings(tmp_path: Path, capsys) -> None:
    path = tmp_path / "data.txt"
    path.write_text(
        "Иванов Иван Иванович\n    математика:80\n",
        encoding="utf-8",
    )

    assert main(["-p", str(path)]) == 0
    output = capsys.readouterr().out
    assert "Students:" in output
    assert "Ratings:" in output
    assert "80.0" in output


def test_main_rejects_unsupported_extension(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text("{}", encoding="utf-8")

    with pytest.raises(ValueError, match="TXT files only"):
        main(["-p", str(path)])
