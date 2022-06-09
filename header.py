import requests
from urllib import request
from bs4 import BeautifulSoup
import nltk
import csv
import re
import datetime as dt
import os
import pickle
import time
from collections import defaultdict
from konlpy.tag import *
import itertools
import pandas

# URL
BASE_URL_MINOR = "https://gall.dcinside.com/mgallery/board/lists"
BASE_URL_MAJOR = "https://gall.dcinside.com/board/lists"
Domain_URL = "https://gall.dcinside.com"

# 헤더 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}




