"""
These areclibraries that is realized from ABC \
that provides simplified method of parsing \
an input file of defined extension.
"""

from typing import List
from QuoteEngine import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface

from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TXTIngestor import TXTIngestor

class Ingestor(IngestorInterface):
    """
    Create a strategic class that realizes \
    from ABC that uses different strategic objects \
    to handle different file types. This abstract base class
    """

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

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