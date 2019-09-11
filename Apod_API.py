import sys
import json
import urllib
import requests
import csv


copyRight = []
date = []
explanation = []
hdurl = []
media_type = []
service_version = []
title = []
url = []


request = urllib.request.Request('https://api.nasa.gov/planetary/apod?api_key=9u4hD1uCMKq9VjsPNDmrSQ0D5WUNGruXrox60WIu&start_date=2017-07-08&end_date=2017-07-10')
opener = urllib.request.build_opener()
response = opener.open(request)
date_JS = json.loads(response.read())
for j in date_JS:
    cp = j.get("copyright",'None')
    copyRight.append(cp)
    date.append(j['date'])
    explanation.append(j['explanation'])
    hdurl.append(j['hdurl'])
    media_type.append(j['media_type'])
    service_version.append(j['service_version'])
    title.append(j['title'])
    url.append(j['url'])


for y in range(0, len(hdurl)):
    print(  'CopyRight = '+copyRight[y] +' \n'
            +'Date = '+date[y]+' \n'
            + 'Explanation = '+explanation[y]+' \n'
            + 'HDURL = '+hdurl[y]+' \n'
            + 'Media Type = '+media_type[y]+' \n'
            + 'Service Version = '+service_version[y]+' \n'
            + 'Title = '+title[y]+' \n'
            + 'URL = '+url[y]+' \n')
