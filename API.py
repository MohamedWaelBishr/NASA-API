import sys
import json
import urllib
import requests

###########################################################################################
request = urllib.request.Request('https://epic.gsfc.nasa.gov/api/natural/all')
opener = urllib.request.build_opener()
response = opener.open(request)

data_JS = json.loads(response.read())
date_list = []
for i in data_JS:
    date_list.append(i['date'])

###########################################################################################
for i in date_list:
    request = urllib.request.Request('https://epic.gsfc.nasa.gov/api/natural/date/'+i)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    date_JS = json.loads(response.read())
    print('Images Of The Day [ '+i+' ]')
    print('###########################################################')
    for j in date_JS:
        print('http://epic.gsfc.nasa.gov/epic-archive/jpg/'+j['image']+'.jpg')
    print('###########################################################')
