"""
Creates a library to load data from PDF files.

A 'PDF_Ingestor' class to parse the PDF file & extract
message body & author, using it to return a collection of
concrete class objects.
"""

from typing import List
import os
import subprocess
import random

from .TXTIngestor import TXTIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """
    Loads & parses data from PDF files.

    :param allowed_extensions - Look for file extension 'pdf'.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the data from PDF file and return 
        a collection of 'Quotes' class objects.

        :param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception(f'cannot ingest PDF files: {path} exception')

        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r", encoding='utf-8-sig')
        quotes_list = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                meme_msg = QuoteModel(str(parse[0]), str(parse[1]))
                quotes_list.append(meme_msg)

        file_ref.close()
        os.remove(tmp)
        return quotes_list