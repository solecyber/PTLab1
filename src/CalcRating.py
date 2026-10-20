"""Average rating calculation."""

from src.Types import DataType

RatingType = dict[str, float]


class CalcRating:
    """Calculate the average grade for every student."""

    def __init__(self, data: DataType) -> None:
        self.data = data

    def calc(self) -> RatingType:
        """Return each student's arithmetic mean grade."""
        rating: RatingType = {}
        for student, subjects in self.data.items():
            if not subjects:
                raise ValueError(f"Student has no grades: {student}")
            rating[student] = sum(score for _, score in subjects) / len(
                subjects
            )
        return rating
