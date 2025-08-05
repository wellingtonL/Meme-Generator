""" an abstract base class library 
that parses an input file of extension."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Created a class with methods to load 
    and parse csv, docx, pdf, txt file.

    :allowed_extensions - Collection of file extension
    """

    allowed_extensions = []
    """file extensions."""

    """IngestorInterface defines two methods with the following class methods"""  
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Returns true if the file has extension 
        and can be loaded and parsed.

        :path: directory of the file
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method which can be encapsulated 
        by user-defined helper classes realized 
        from the ABC."""
        pass