import requests
import os
def GET(url):
  r = requests.get(url)
  return r.text

def RUN(cmd):
  return os.system(cmd)

def PIPE(cmd):
  return os.popen(cmd).read()

def DOWNLOAD(url, filename):
  cmd = f"curl -o download/{ filename } { url }"
  RUN(cmd)

def NORMALIZE(string):
  return string.replace(' ', '-').replace("'", '').replace('"', '') + '.pdf'