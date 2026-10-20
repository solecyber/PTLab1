"""Reader for the XML format required by variant 10."""

from xml.etree import ElementTree

from src.DataReader import DataReader
from src.Types import DataType


class XMLDataReader(DataReader):
    """Read student grades from a structured XML document."""

    def read(self, path: str) -> DataType:
        """Parse *path* and return grades in the project's common format."""
        try:
            root = ElementTree.parse(path).getroot()
        except ElementTree.ParseError as error:
            raise ValueError("Invalid XML document") from error

        if root.tag != "students":
            raise ValueError("The root element must be <students>")

        students: DataType = {}
        for student_element in root.findall("student"):
            student_name = student_element.get("name", "").strip()
            if not student_name:
                raise ValueError("Every student must have a name")
            if student_name in students:
                raise ValueError(f"Duplicate student: {student_name}")

            subjects: list[tuple[str, int]] = []
            for subject_element in student_element.findall("subject"):
                subject_name = subject_element.get("name", "").strip()
                score_text = subject_element.get("score", "")
                try:
                    score = int(score_text)
                except ValueError as error:
                    raise ValueError(
                        f"Invalid score for student: {student_name}"
                    ) from error

                if not subject_name or not 0 <= score <= 100:
                    raise ValueError(
                        f"Invalid subject for student: {student_name}"
                    )
                subjects.append((subject_name, score))

            if not subjects:
                raise ValueError(f"Student has no grades: {student_name}")
            students[student_name] = subjects

        if not students:
            raise ValueError("The XML document contains no students")
        return students
