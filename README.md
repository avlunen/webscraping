# Webscraping
Various Python scripts to scrape data from web pages, such as Wikipedia (yes, I know there is Wikidata; I have used it, but I found that sometimes there isn't the same data available). The scripts are specific to the structures of pages I was interested in; which also means they may change anytime. The Wikipedia scripts scrape data from lists on pages, and then retrieves the coordinates for each place from the individual Wikipedia entry for it. The data is then output as CSV file, so that it can be loaded and mapped in a GIS.

Most of these scripts I hacked together quickly to get some data for a history of the Holocaust module I teach at university, so that students have something to map.

wikipedia_camps.py: Extracting the data for Nazi concentration camps.

wikipedia_camps.csv: Data file resulting from a test run of the above.

wikipedia_shtetl.py: Extracting the data for Jewish towns (shtetl) and cities (shtot) in East Central Europe.

wikipedia_shtetl.csv: Data file resulting from a test run of the above.

wikipedia_shtot.csv: Data file resulting from a test run of the above.
