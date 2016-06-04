from bs4 import BeautifulSoup
import requests
import sys
import re

if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    from urllib import parse
    py_ver = 3
else:
    # Python 2 code in this block
    from urlparse import urlparse
    py_ver = 2


page = requests.get("https://plex.tv/downloads")

soup = BeautifulSoup(page.text, 'html.parser')
centos_url = soup.find( attrs={'data-event-label': 'CentOS64'})['href']

url_path=urlparse(centos_url).path
# url_path /plex-media-server/0.9.16.6.1993-5089475/plexmediaserver-0.9.16.6.1993-5089475.x86_64.rpm

plex_ver = re.split('\/', url_path)[2]

print(plex_ver)
