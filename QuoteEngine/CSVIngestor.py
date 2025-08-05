"""
Creates a library that loads data from CSV files.
A 'CSV_Ingestor' class will parse the CSV file and extract
message body and author, using this file to return a collection of
class objects.

"""
from typing import List
import pandas as pd

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
 

class CSVIngestor(IngestorInterface):
    """
    Loads & parses data from CSV files.

    :param for allowed_extensions - Look for file extension 'csv'.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the data from CSV file and return 
            collection of 'Quotes' class objects.

        :path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception("can ingest CSV Files only exception")

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            try:
                meme_msg = QuoteModel(row['body'], row['author'])
                quotes.append(meme_msg)
            except Exception as e:
                print(f"Error parsing row {index}: {e}")
            else:
                    quotes.append(meme_msg)

        return quotes