# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# ME: import scraper wiki libary to store data
import scraperwiki
import lxml.html
#
print "Hello World"
myname="Sally"
print myname
# # Read in a page
#ME: replace foo.com with site you want to scrape
html = scraperwiki.scrape("http://foo.com")
print html
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print root
root.cssselect("a")
selectstuff = root.cssselect("div[align='left']")
print selectstuff
for i in selectstuff:
  print i.text #.txt grabs text content of tags
  print i.attrib['href']#.attrib grabs the value of the attribute specified
  

#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
