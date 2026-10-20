"""Abstract interface for student data readers."""

from abc import ABC, abstractmethod

from src.Types import DataType


class DataReader(ABC):
    """Define the interface implemented by all input readers."""

    @abstractmethod
    def read(self, path: str) -> DataType:
        """Read student grades from *path*."""
        raise NotImplementedError
