import sys
import json
import urllib
import requests

Search = input("Please Enter , What Are You Searching For On Nasa ?    ")
h = str.lower(Search)
f = str.split(h, ' ')
Search_Final = '%'.join(f)
count = int(input("Please Enter Number Of Result You Want From 1 To 50 Per Once [The Large Number The Long Search Time] :  "))
print('\n\n')
print(' |||||||||||||||||  Please Wait That May Take Some Time  ||||||||||||||||| '+'\n\n')
###########################################################################################
request = urllib.request.Request("https://images-api.nasa.gov/search?q="+Search_Final+"&media_type=image")
opener = urllib.request.build_opener()
response = opener.open(request)
data_JS = json.loads(response.read())
Description = []
Nasa_ID = []
Title = []
ImgLinks=[]

try:
    for x in range(count):
        Title.append(data_JS['collection']['items'][x]['data'][0]['title'])
        Nasa_ID.append(data_JS['collection']['items'][x]['data'][0]['nasa_id'])
        Description.append(data_JS['collection']['items'][x]['data'][0]['description'])
    #geting image link for nasa id
    for ID in Nasa_ID:
        request = urllib.request.Request('https://images-api.nasa.gov/asset/'+ID)
        opener = urllib.request.build_opener()
        response = opener.open(request)
        data_KS = json.loads(response.read())
        ImgLinks.append(data_KS['collection']['items'][0]['href'] )

    print('###########################################################################################')
    l = len(Description)
    for ll in range(l):
        print('Nasa_Id -> '+Nasa_ID[ll]+'\n'
            +'Title -> '+Title[ll]+'\n'
            +'Description -> '+Description[ll]+'\n'
            +'Image Link -> '+ImgLinks[ll]+'\n'
            )
        print('###########################################################################################')
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
except:
    print("We Are Very Sorry :( , No Result Found , Try Other Words Next Time")
