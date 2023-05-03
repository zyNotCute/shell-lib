import re
from bs4 import BeautifulSoup
from const import *
from util import *

def search(book_name):
  result_id = 0
  search_result = []
  url_search_template = "search.php?req={}&open=0&res=25&view=simple&phrase=1&column=def"
  soup = BeautifulSoup(GET(URL_BASE + url_search_template.format(book_name)), "html.parser")
  res = soup.find_all('tr')
  res = [ node for node in res if node.find('td', string='pdf') ]
  for node in res:
    author, title = node.find_all('td')[1].get_text(), node.find_all('td')[2].get_text()
    link = URL_BASE + node.find('a', href=re.compile(BOOK_INDEX_KEYWORD)).get('href')
    if not author:
      author = 'Unknown'
    if not title:
      title = 'Unknown'
    if len(title) > LINE_MAX_LENGTH:
      title = title[:LINE_MAX_LENGTH] + '...'
    search_result.append(link)
    print(
      f"""
      Result ID:  { result_id }
      Title:      { title }
      Author:     { author }
      """
    )
    result_id += 1
  return search_result