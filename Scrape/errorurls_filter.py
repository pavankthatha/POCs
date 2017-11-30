from bs4 import BeautifulSoup
import urllib.request
import re

url_handle = open('/tmp/POCs-master/Scrape/html_urls','r')
urls = url_handle.readlines()
actual_url_list = []
for each_url in urls:
    actual_url_list.append(each_url.strip('\n'))

for url in actual_url_list:
    try:
        html = urllib.request.urlopen(url) # put the url here
    except:
        print (url)
        pass

