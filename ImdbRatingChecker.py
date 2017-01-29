# Name: Gunvant Sarpate          
# Email : sarpate007@gmail.com
# Date of Creation26Jan2016 1.50AM


import urllib2
from bs4 import BeautifulSoup
import json
import sys


title = raw_input("Enter Movie Name\n")
url = "http://www.omdbapi.com/?t="+title
response = urllib2.urlopen(url).read()
jsonvalues = json.loads(response)

if jsonvalues["Response"]== "True":
    rating = jsonvalues["imdbRating"]
    year = jsonvalues["Year"]
    director = jsonvalues["Director"]
    language = jsonvalues["Language"]
else:
    print "Error while fetching data"
    
print "Year of release = "+year
print "IMDB Rating= "+rating
print "Director = "+director
print "Language = "+language
raw_input()
