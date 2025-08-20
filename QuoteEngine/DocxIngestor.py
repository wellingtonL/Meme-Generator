"""
Creates a library that loads data from CSV files.

A 'CSV_Ingestor' class will parse the CSV file and extract
message body and author, using to return a collection of
concrete class objects.
"""
import docx
from typing import List
from .QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface

 

class DocxIngestor(IngestorInterface):
    """
    Loads & parses data from files.
    param allowed_extensions - Look for file extension 'docx'.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Function Parses the data from DOCXfile and returns 
        a collection of 'Quotes' class objects.

        param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception("can ingest Docx only exception")


        doc = docx.Document(path)
        quotes =[]

        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split(' - ')
                meme_msg = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(meme_msg)
        return quotes
                
                