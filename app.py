#Meme Generator Flask App.
from flask import Flask, render_template, request
import requests
import random
import os

from QuoteEngine.Ingestor import Ingestor
from MemeEngine.MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup() -> tuple[list, list[str]]:
    # Load all resources 

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    """
    Use the Ingestor class to parse all files in the
    quote_files variable
    """
    quotes_list= []
    for file in quote_files:
        try:
            quotes_list.extend(Ingestor.parse(file))
        except Exception as e:
            print(f"Error parsing: " + file + " due to: " + str(e))

    images_path = "./_data/photos/dog/"
    imgs_list = []

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    for filename in os.listdir(images_path):
        if filename.endswith('.jpg'):
            imgs_list.append(os.path.join(images_path, filename))

    return quotes_list, imgs_list
quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """ Generate a random meme """


    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    try:
        img = random.choice(imgs)
        quote = random.choice(quotes)
        path = meme.make_meme(img, quote.body, quote.author)
        return render_template('meme.html', path=path)
    except Exception as e:
        print(f"Error generating meme: " + str(e))
        return render_template('error.html', error=str(e))

@app.route('/create', methods=['GET'])
def meme_form():
    """
    User input for meme information.
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
 
    img = f'./{random.randint(0,10000)}_tmp.jpg'
    img_url = request.form.get('image_url')
    extension = img_url.split('.')[-1]
    #temp = 'tmp-{}.{}'.format(str(img),extension)
    response = requests.get(img_url).content
        # print(image_url)

    with open(img, 'wb') as f:
            f.write(response)
            quote_body = request.form.get('body', '')
            quote_author = request.form.get('author', 'unknown')
            path = meme.make_meme(img, quote_body, quote_author)
            os.remove(img)

        #r = requests.get(image_url)
        # print(r)
        #tmp_img = f'./{random.randint(0,10000)}_tmp.jpg'
        #img = open(tmp_img, 'wb').write(r.content)
   
    #path = meme.make_meme(tmp_img, quote_body, quote_author)
    # print(tmp_img)
    #os.remove(tmp_img)

    return render_template('meme.html', path=path)
    


if __name__ == '__main__':
    app.run(debug=True)
