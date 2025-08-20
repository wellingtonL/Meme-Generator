#Creates a library to generate memes.
import os
import random

from PIL  import Image, ImageFont, ImageDraw
from typing import List


class MemeEngine():
    """Creates a meme and saves it in the output folder."""

    def __init__(self, out_path: str)-> List:
        """Initialize meme object with user-defined
        output path to save the meme."""
        os.makedirs(out_path, exist_ok=True)
        self.out_path = out_path

    def make_meme(self, img_path, msg_body=None, msg_author=None, width=500) -> str:
        """Resizes input image to a max width of 400 pixels
        while maintaining the aspect ratio. Draw message
        quote and author on the meme.

        Function parameters
        :param img_path = Path contains the meme image
        :param msg_body = Message text quote to be written on the image
        :param msg_author = Message's author to be written on the image
        :param width = Width of the image to be resized
        """
        
        #Image.open(img_path) as img:
        
        img = Image.open(img_path)
        
        
        #resize image
        if not width:
           width = 500
        ratio = img.width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((int(width), int(height)), Image.NEAREST)

        if msg_body is not None and msg_author is not None:
                complete_msg = f'{msg_body}\n- {msg_author}'
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./_data/fonts/ARLRDBD.ttf', size=25)
                draw.text((10, 20), complete_msg, font=font, fill='purple')

        final_out_path = f'{random.randint(0,10000000)}.jpeg'
        out_path = f'{self.out_path}/{final_out_path}'
        img.save(out_path)
        try:
            img.close()
        except Exception as e:
            print("Error: when trying to close image. Context:   ", e)
            return None
        
        return out_path