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
    try:
        soup = BeautifulSoup(html.read(), 'html.parser')
    except:
        pass
    try:    
        texts = soup.findAll(text=True)
    except:
        pass
    
    def visible(element):
         if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
         elif re.match('<!--.*-->', str(element)):
            return False
         elif re.match('[if * <![endif]', str(element)):
            return False
         return True
    try:
        visible_texts = filter(visible, texts)
    except:
        pass
    '''
     write the texts into a txt file
    '''
    with open('amazon_vox.txt', 'bw') as outfile: #define the location of the output
        try:
            for text in visible_texts:
                try:
                    print(text.encode('utf-8'))
 
                    outfile.write(text.encode('utf-8'))
                except:
                    pass
        except:
            pass
