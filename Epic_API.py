import sys
import json
import urllib
import requests
import csv

Date =''
Images=[]
###########################################################################################
request = urllib.request.Request('https://epic.gsfc.nasa.gov/api/natural/all')
opener = urllib.request.build_opener()
response = opener.open(request)

data_JS = json.loads(response.read())
date_list = {}
for i in data_JS:
    date_list[i['date']] = ''

d_l =[]
#print(date_list)
###########################################################################################
download_dir = "Date_Image_Dataset_NASA.csv"  # where you want the file to be downloaded to

csv = open(download_dir, "w")
#"w" indicates that you're writing strings to the file

columnTitleRow = "Date, Images \n"
csv.write(columnTitleRow)

value=''
for i in date_list.keys():
    request = urllib.request.Request('https://epic.gsfc.nasa.gov/api/natural/date/'+i)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    date_JS = json.loads(response.read())
    for j in date_JS:
        value += 'http://epic.gsfc.nasa.gov/epic-archive/jpg/' + j['image'] +'.jpg  |  ' 
    date_list[i] = value
    print('Date  -> '+i+' Value -> '+'\n'+date_list[i])
    value=''
    string = str(i) + ','+ str(date_list[i]) + ' ' + '\n'
    csv.write(string)
