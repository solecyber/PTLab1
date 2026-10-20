"""Reader for the text format used in the base assignment."""

from src.DataReader import DataReader
from src.Types import DataType


class TextDataReader(DataReader):
    """Read students and grades from an indented text file."""

    def read(self, path: str) -> DataType:
        students: DataType = {}
        current_student: str | None = None

        with open(path, encoding="utf-8") as file:
            for line_number, raw_line in enumerate(file, start=1):
                if not raw_line.strip():
                    continue

                if not raw_line[0].isspace():
                    current_student = raw_line.strip()
                    students[current_student] = []
                    continue

                if current_student is None:
                    raise ValueError(
                        f"Grade before student name at line {line_number}"
                    )

                try:
                    subject, score_text = raw_line.split(":", maxsplit=1)
                    score = int(score_text.strip())
                except ValueError as error:
                    raise ValueError(
                        f"Invalid grade at line {line_number}"
                    ) from error

                subject = subject.strip()
                if not subject or not 0 <= score <= 100:
                    raise ValueError(
                        f"Invalid grade at line {line_number}"
                    )
                students[current_student].append((subject, score))

        return students
