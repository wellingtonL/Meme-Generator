
# -*- coding: utf-8 -*-
"""
Creates a library to load data from TXT files.
 TXTIngestor class will parse the TXT file & extract
message body & author, using it to return a collection of
concrete class objects.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """
    Loads and parses data from TXT files.
    :param allowed_extensions - Look for file extension 'txt'.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the data from TXT file and return
            a collection of 'Quotes' class objects.
            :param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception(f'cannot ingest TXT files only exception')
        
        #file_ref = path.string.split('.')[-1]
        file_ref = open(path, encoding="UTF-8")
        quotes = []

                
        #with open(path, 'r') as file_ref:
        #    file_ref = file_ref.readlines()
            
        for line in file_ref.readlines():
            try:
                
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                #file_ref= path.string.split('.')[-1]
                meme_msg = QuoteModel(parse[0].strip(), parse[1].strip())
            except Exception as e:
                print(f"Error parsing line: due to "+str(e))
                
            else:    
                quotes.append(meme_msg)
                #raise Exception(f'can ingest TXT files {file_ref} only exception')
        file_ref.close()    
        return quotes
    