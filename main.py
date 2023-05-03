import sys
from util import *
from search import search
from download import download

if sys.argv[1] == 'find':
  search_result = search(sys.argv[2])
  id = input('Input the result ID of the book you want to download (q to quit): ')
  if id == 'q':
    exit()
  id = int(id)
  index_url = search_result[id]
  download(index_url, NORMALIZE(sys.argv[2]))
  exit()

if sys.argv[1] == 'cat':
  ls = PIPE('ls download')
  ls = [ line for line in ls.split('\n') ][:-1]
  ls_cpy = []
  for i in range(len(ls)):
    ls_cpy.append(str(i) + ': ' + ls[i])
  print('\n'.join(ls_cpy))
  id = input('Input the ID of the book you want to read (q to quit): ')
  if id == 'q':
    exit()
  id = int(id)
  RUN('xdg-open download/' + ls[id])
  exit()

if sys.argv[1] == 'rm':
  ls = PIPE('ls download')
  ls = [ line for line in ls.split('\n') ][:-1]
  ls_cpy = []
  for i in range(len(ls)):
    ls_cpy.append(str(i) + ': ' + ls[i])
  print('\n'.join(ls_cpy))
  id = input('Input the ID of the book you want to read (q to quit): ')
  if id == 'q':
    exit()
  id = int(id)
  RUN('rm download/' + ls[id])
  exit()

if sys.argv[1] == 'chsrc':
  RUN(f"echo 'URL_BASE = { sys.argv[2] }' > conf.py")