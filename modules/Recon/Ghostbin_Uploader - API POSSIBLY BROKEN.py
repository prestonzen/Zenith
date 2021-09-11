#!/usr/bin/python

import requests
import sys
from bs4 import BeautifulSoup as bs

if not len(sys.argv[1:]):
   print('\n\tGhostBin Poster. Input file -> Base64 -> ghostbin.com')
   print('\n\tUsage: ghostbin-post [filename]\n')
   exit()

f = open(sys.argv[1],'rb')
paste_text = f.read().encode('base64').replace('\n','')
f.close()
print(paste_text)

paramsPost = {"password":"","text":paste_text,"lang":"text","title":"","expire":"14d"}
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0","Referer":"https://ghostbin.com/","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Content-Type":"application/x-www-form-urlencoded"}
response = requests.post("https://ghostbin.com/paste/new", data=paramsPost, headers=headers)

#print response.status_code
rdata = bs(response.content)
a = rdata.find_all('title')[0].text
url = 'https://ghostbin.com/paste/'+a.split(' ')[0]+'/raw'
print ('\nwget %s -O /tmp/mmm && cat /tmp/mmm | base64 -d' % url)
print ('\ncurl -s %s | base64 -d\n' % url)