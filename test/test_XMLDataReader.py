"""Tests for the XML reader required by variant 10."""

from pathlib import Path

import pytest

from src.XMLDataReader import XMLDataReader


def write_xml(tmp_path: Path, content: str) -> str:
    """Write a test document and return its path."""
    path = tmp_path / "students.xml"
    path.write_text(content, encoding="utf-8")
    return str(path)


def test_read_parses_xml_file(tmp_path: Path) -> None:
    path = write_xml(
        tmp_path,
        """<?xml version="1.0" encoding="UTF-8"?>
<students>
  <student name="Иванов Иван Иванович">
    <subject name="математика" score="60" />
    <subject name="программирование" score="91" />
  </student>
  <student name="Петров Петр Петрович">
    <subject name="химия" score="87" />
  </student>
</students>
""",
    )

    assert XMLDataReader().read(path) == {
        "Иванов Иван Иванович": [
            ("математика", 60),
            ("программирование", 91),
        ],
        "Петров Петр Петрович": [("химия", 87)],
    }


@pytest.mark.parametrize(
    ("content", "message"),
    [
        ("<students>", "Invalid XML document"),
        ("<root />", "root element"),
        ("<students />", "contains no students"),
        (
            "<students><student /></students>",
            "must have a name",
        ),
        (
            "<students><student name='A' /><student name='A' />"
            "</students>",
            "Duplicate student",
        ),
        (
            "<students><student name='A' /></students>",
            "has no grades",
        ),
        (
            "<students><student name='A'>"
            "<subject name='math' score='x' />"
            "</student></students>",
            "Invalid score",
        ),
        (
            "<students><student name='A'>"
            "<subject name='' score='90' />"
            "</student></students>",
            "Invalid subject",
        ),
        (
            "<students><student name='A'>"
            "<subject name='math' score='101' />"
            "</student></students>",
            "Invalid subject",
        ),
    ],
)
def test_read_rejects_invalid_xml(
    content: str,
    message: str,
    tmp_path: Path,
) -> None:
    with pytest.raises(ValueError, match=message):
        XMLDataReader().read(write_xml(tmp_path, content))
