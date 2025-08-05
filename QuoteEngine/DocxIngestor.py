"""
Creates a library that loads data from CSV files.

A 'CSV_Ingestor' class will parse the CSV file and extract
message body and author, using to return a collection of
concrete class objects.

"""
from typing import List
import docx


from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    Loads & parses data from files.

    :param allowed_extensions - Look for file extension 'csv'.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
           Function Parses the data from DOCXfile and returns 
        a collection of 'Quotes' class objects.

        :param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception("can ingest Docx only exception")

        quotes = []
        doc= docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split(' - ')
                meme_msg = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(meme_msg)
        return quotes
                
                