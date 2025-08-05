import argparse

def build_parser():
    """Create a parser to parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Meme Generator tool.")
    parser.add_argument('--body', help="a string quote body", default="I met a happy dog, who taught me how to smile.")
    parser.add_argument('--author', help="a string quote author", default="Samuel Beckett")
    parser.add_argument('--path', help="an image path", default='./_data/photos/dog/xander_1.jpg')
    return parser