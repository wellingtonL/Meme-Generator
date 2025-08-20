"""
These areclibraries that is realized from ABC \
that provides simplified method of parsing \
an input file of defined extension.
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """
    Create a strategic class that realizes \
    from ABC that uses different strategic objects \
    to handle different file types. This abstract base class
    """

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Data is Parse from a file with valid and defined \
        extension, done through strategic object.

        Returns the collection of 'QuoteModel' class objects for
        each file type.

        :param path: Directory of the input file
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                """
                Check if the file is valid or not.
                """
                return ingestor.parse(path)