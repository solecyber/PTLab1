"""Command-line entry point for the laboratory project."""

import argparse
from pathlib import Path
from typing import Sequence

from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader


def get_path_from_arguments(args: Sequence[str] | None = None) -> str:
    """Parse and return the input file path."""
    parser = argparse.ArgumentParser(description="Student grade processing")
    parser.add_argument(
        "-p",
        "--path",
        required=True,
        help="path to a TXT or XML data file",
    )
    return parser.parse_args(args).path


def main(args: Sequence[str] | None = None) -> int:
    """Read a text file and print average ratings."""
    path = get_path_from_arguments(args)
    if Path(path).suffix.lower() != ".txt":
        raise ValueError("The base project supports TXT files only")

    students = TextDataReader().read(path)
    ratings = CalcRating(students).calc()

    print("Students:", students)
    print("Ratings:", ratings)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
