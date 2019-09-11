import sys
import json
import urllib
import requests

#"https://images-api.nasa.gov/search?q=apollo%2011&description=moon%20landing&media_type=image"
###########################################################################################
request = urllib.request.Request("https://images-api.nasa.gov/search?q=apollo%2011&media_type=image")
opener = urllib.request.build_opener()
response = opener.open(request)

data_JS = json.loads(response.read())
Description = []
Nasa_ID = []
Title = []
count = 10
for x in range(count):
    print(data_JS['collection']['items'][x]['data'][0]['title'])
    print('-------------------------------------------------------------------------')
    print(data_JS['collection']['items'][x]['data'][0]['nasa_id'])
    print('-------------------------------------------------------------------------')
    print(data_JS['collection']['items'][x]['data'][0]['description'])
    print('-------------------------------------------------------------------------')
    print(data_JS['collection']['items'][x]['links'][0]['href'])
    print('-------------------------------------------------------------------------')
###########################################################################################
""" for i in date_list:
    request = urllib.request.Request(
        'https://epic.gsfc.nasa.gov/api/natural/date/'+i)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    date_JS = json.loads(response.read())
    print('Images Of The Day [ '+i+' ]')
    print('###########################################################')
    for j in date_JS:
        print('http://epic.gsfc.nasa.gov/epic-archive/jpg/'+j['image']+'.jpg')
    print('###########################################################')
 """
