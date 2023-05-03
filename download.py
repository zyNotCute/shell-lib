from util import *
from bs4 import BeautifulSoup
from const import *
def get_book_mirror_url(book_index_url):
  soup = BeautifulSoup(GET(book_index_url), "html.parser")
  res = soup.find('a', string=BOOK_MIRROR_KEYWORD)
  return res.get('href')

def get_book_download_url(book_mirror_url):
  soup = BeautifulSoup(GET(book_mirror_url), "html.parser")
  res = soup.find('a', string=BOOK_DOWNLOAD_KEYWORD)
  return res.get('href')

def download(book_index_url, book_name):
  book_mirror_url = get_book_mirror_url(book_index_url)
  book_download_url = get_book_download_url(book_mirror_url)
  DOWNLOAD(book_download_url, book_name)