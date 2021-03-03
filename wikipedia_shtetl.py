#-------------------------------------------------------------------------------
# Name:        wikipedia_shetl.py
# Purpose:
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

# extract coordinates from Wikipedia geo page
def get_coords(link):
   gheader = {'User-Agent': 'Mozilla/5.0'} # Needed to prevent 403 error on Wikipedia
   greq = urllib2.Request(link,headers=gheader)
   gpage = urllib2.urlopen(greq)
   gsoup = BeautifulSoup(gpage)

   geo = gsoup.find('span', {'class' : 'geo'})

   if geo <> None: g = geo.get_text()
   else: g = None

   return g

# extract Shtelekh from Wikipedia page; these are present as bullet point list on the page
def shtetl():
   wiki = "https://en.wikipedia.org/wiki/List_of_shtetls"
   header = {'User-Agent': 'Mozilla/5.0'} # Needed to prevent 403 error on Wikipedia
   req = urllib2.Request(wiki,headers=header)
   page = urllib2.urlopen(req)
   soup = BeautifulSoup(page)

   f = codecs.open("wikipedia_shtetl.csv", "w", "utf-8")
   f.write("Latitude;Longitude;City;URL\n")

   for li in soup.findAll("li"): # the shtetl are all in UL lists, the <li> elements having a title attribute
      a = li.findAll("a", title=True)
      if len(a) > 0:
         if a[0].has_key('href') and a[0]['href'].startswith('/wiki') and ':' not in a[0]['href']:
            city = a[0]['title']
            url = a[0]['href']

            geo = get_coords("https://en.wikipedia.org"+url)
            if geo == None:
               lat = "n/a"
               lon = "n/a"
            else:
               lat = geo.split(";")[0]
               lon = geo.split(";")[1]

            print city
            f.write(lat.strip()+";"+lon.strip()+";"+city+";"+"https://en.wikipedia.org"+url+"\n")

   f.close()

# extract Shots; these are in their separate table on the page
def shtot():
   wiki = "https://en.wikipedia.org/wiki/List_of_shtetls"
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

   f = codecs.open("wikipedia_shtot.csv", "w", "utf-8")

   f.write("Latitude;Longitude;City;Yiddish;Romanized;Pre-WW2-Population;URL\n")

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
   shtetl()
   shtot()

if __name__ == '__main__':
    main()