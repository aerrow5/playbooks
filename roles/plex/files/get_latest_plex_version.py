import requests
import sys
import re

if (sys.version_info > (3, 0)):
    from urllib import parse
    py_ver = 3
else:
    from urlparse import urlparse
    py_ver = 2

r = requests.get("https://plex.tv/api/downloads/1.json")

j = r.json()

for i in j['computer']['Linux']['releases']:
    if 'CentOS 64-bit' in i['label']:
        centos_json = i
        break

# We have full URL:
# 'https://downloads.plex.tv/plex-media-server/1.3.3.3148-b38628e/plexmediaserver-1.3.3.3148-b38628e.x86_64.rpm
plex_ver = re.split('\/', centos_json['url'])[4]

print(plex_ver)
