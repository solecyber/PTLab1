"""Command-line entry point for the laboratory project."""

import argparse
from pathlib import Path
from typing import Sequence

from src.CalcRating import CalcRating
from src.DataReader import DataReader
from src.TextDataReader import TextDataReader
from src.XMLDataReader import XMLDataReader


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


def get_reader(path: str) -> DataReader:
    """Select an input reader by file extension."""
    readers = {
        ".txt": TextDataReader,
        ".xml": XMLDataReader,
    }
    suffix = Path(path).suffix.lower()
    try:
        return readers[suffix]()
    except KeyError as error:
        raise ValueError(f"Unsupported input format: {suffix}") from error


def main(args: Sequence[str] | None = None) -> int:
    """Read a supported data file and print average ratings."""
    path = get_path_from_arguments(args)

    students = get_reader(path).read(path)
    ratings = CalcRating(students).calc()

    print("Students:", students)
    print("Ratings:", ratings)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
