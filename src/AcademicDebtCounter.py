"""Academic debt calculation required by variant 10."""

from src.Types import DataType


class AcademicDebtCounter:
    """Find students who have grades below 61 in exactly two subjects."""

    PASSING_SCORE = 61
    REQUIRED_DEBT_COUNT = 2

    def __init__(self, data: DataType) -> None:
        self.data = data

    def student_names(self) -> list[str]:
        """Return names of students matching the variant 10 condition."""
        result = []
        for student, subjects in self.data.items():
            debt_count = sum(
                score < self.PASSING_SCORE for _, score in subjects
            )
            if debt_count == self.REQUIRED_DEBT_COUNT:
                result.append(student)
        return result

    def count(self) -> int:
        """Return the number of students matching the condition."""
        return len(self.student_names())
