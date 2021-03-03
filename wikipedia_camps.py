#-------------------------------------------------------------------------------
# Name:        wikipedia_camps.py
# Purpose:     Extract names and data for Nazo concentration camps from Wikipedia
#              and save the data as CSV file
#
# Author:      Alexander von Lünen
#
# Created:     19/11/2017
# Copyright:   (c) avl 2016
# Licence:     Public Domain
#-------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import urllib2
import codecs

# extract ccordinates from pages for individual camps
def get_coords(link):
   gheader = {'User-Agent': 'Mozilla/5.0'} # Needed to prevent 403 error on Wikipedia
   greq = urllib2.Request(link,headers=gheader)
   gpage = urllib2.urlopen(greq)
   gsoup = BeautifulSoup(gpage)

   geo = gsoup.find('span', {'class' : 'geo'})

   if geo <> None: g = geo.get_text()
   else: g = None

   return g

# extract camp data from the page
def camps():
   wiki = "https://en.wikipedia.org/wiki/List_of_Nazi_concentration_camps"
   header = {'User-Agent': 'Mozilla/5.0'} # Needed to prevent 403 error on Wikipedia
   req = urllib2.Request(wiki,headers=header)
   page = urllib2.urlopen(req)
   soup = BeautifulSoup(page)

   url = ""
   city = ""
   yiddish = ""
   roman = ""
   pre_ww2_pop = ""

   table = soup.find("table", { "class" : "wikitable sortable" })

   f = codecs.open("wikipedia_camps.csv", "w", "utf-8")

   f.write("Latitude;Longitude;Name;country_today;camp_type;dates;Prisoners;Deaths;URL\n")

   for row in table.findAll("tr"):
       cells = row.findAll("td")
       #For each "tr", assign each "td" to a variable.
       if len(cells) == 5:
           url = cells[1].find_all('a')[0].get('href')
           if url == None: url = ""
           city = cells[1].find(text=True)
           if city == None: city = ""
           yiddish = cells[2].find(text=True)
           if yiddish == None: yiddish = ""
           roman = cells[3].find(text=True)
           if roman == None: roman = ""
           pre_ww2_pop = cells[4].find(text=True)
           if pre_ww2_pop == None: pre_ww2_pop = ""

           print str(roman)

           geo = get_coords("https://en.wikipedia.org"+url)
           if geo == None:
               lat = "n/a"
               lon = "n/a"
           else:
               lat = geo.split(";")[0]
               lon = geo.split(";")[1]

           f.write(lat.strip()+";"+lon.strip()+";"+city.strip()+";"+yiddish.strip()
               +";"+roman.strip()+";"+pre_ww2_pop.strip()+";"+"https://en.wikipedia.org"+url+"\n")

   f.close()

def main():
   camps()

if __name__ == '__main__':
    main()