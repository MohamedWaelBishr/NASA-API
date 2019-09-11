import sys
import json
import urllib
import requests
import itertools
import threading
import time
import sys
###########################################################################################
Description = []
Nasa_ID = []
Title = []
VidLinks = []
VidSize = []
SubLinks =[]
SubSize = []
Search = input("Please Enter , What Are You Searching For On Nasa ?    ")
h = str.lower(Search)
f = str.split(h, ' ')
Search_Final = '%'.join(f)
count = int(input("Please Enter Number Of Result You Want From 1 To 50 Per Once [The Large Number The Long Search Time] :  "))
print('\n\n')
print(' |||||||||||||||||  Please Wait That May Take Some Time  ||||||||||||||||| '+'\n\n')
###########################################################################################
request = urllib.request.Request('https://images-api.nasa.gov/search?q='+Search_Final+'&media_type=video')
opener = urllib.request.build_opener()
response = opener.open(request)
data_JS = json.loads(response.read())
try :
    for x in range(count):
        Title.append(data_JS['collection']['items'][x]['data'][0]['title'])
        Nasa_ID.append(data_JS['collection']['items'][x]['data'][0]['nasa_id'])
        Description.append(data_JS['collection']['items'][x]['data'][0]['description'])
    # geting video link for nasa id
    for ID in Nasa_ID:
        request = urllib.request.Request('https://images-api.nasa.gov/asset/'+ID)
        opener = urllib.request.build_opener()
        response = opener.open(request)
        data_KS = json.loads(response.read())
        VidLinks.append(data_KS['collection']['items'][0]['href'])
    #geting size of videos
    for d in VidLinks:
        site = urllib.request.urlopen(d)
        meta = site.info()
        s = int(meta.get("Content-Length"))
        ss = s//1000000
        VidSize.append(ss)
    #geting Video SRT Link
    for ID in Nasa_ID:
        request = urllib.request.Request(
            'https://images-api.nasa.gov/captions/' + ID)
        opener = urllib.request.build_opener()
        response = opener.open(request)
        data_OS = json.loads(response.read())
        SubLinks.append(data_OS['location'])
    #geting size of Subtitle
    for g in SubLinks:
        site = urllib.request.urlopen(g)
        meta = site.info()
        s = int(meta.get("Content-Length"))
        ss = s//1000
        SubSize.append(ss)

    ###########################################################################################

    print('###########################################################################################')
    l = len(Description)
    for ll in range(l):
        print('Nasa_Id -> '+Nasa_ID[ll]+'\n'
            + 'Title -> '+Title[ll]+'\n'
            + 'Description -> '+Description[ll]+'\n'
            + 'Video Link -> '+VidLinks[ll] +
            ' ------ [ '+str(VidSize[ll])+']  MB'+'\n'
            + 'Subtitle Link -> '+SubLinks[ll]+' ------ [ '+str(SubSize[ll])+']  KB'+'\n')
        print('###########################################################################################')
    ###########################################################################################
except:
    print("We Are Very Sorry :( , No Result Found , Try Other Words Next Time")