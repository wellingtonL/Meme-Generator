# -*- coding: utf-8 -*-

import environ
from dotenv import dotenv
from os.path import join, dirname

dotenv = environ.Env()
dotenv.read_env(join(dirname(__file__), './env'))

SERVER_PATH = dotenv('SERVER_PATH')
FLASK_PATH = dotenv('FLASK_PATH')
TMP_PATH = dotenv('TMP_PATH')
STATIC_PATH = dotenv('STATIC_PATH')
