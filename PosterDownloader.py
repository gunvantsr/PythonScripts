# Name: Gunvant Sarpate          
# Email : sarpate007@gmail.com
# Date of Creation26Jan2016 1.50AM

import urllib2
import urllib
from bs4 import BeautifulSoup
import json
import webbrowser
import sys

title = raw_input("Enter Movie Name\n")
url = "http://www.omdbapi.com/?t="+title
response = urllib2.urlopen(url).read()
jsonvalues = json.loads(response)

if jsonvalues["Response"]== "True":
    poster = jsonvalues["Poster"]
    urllib.urlretrieve(poster,title+".jpg")
    print "Downloaded!!"
else:
    print "Error while fetching data"


