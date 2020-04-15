import requests
from bs4 import BeautifulSoup
from datetime import datetime

#variables
now = datetime.now()
total = "xxx"
timer = 60000.0
itera = 1

#total live number fetcher (web scraper)
def update():
  page = requests.get("https://www.worldometers.info/coronavirus/country/us/")

  soup = BeautifulSoup(page.content, 'html.parser')

  livenum = str(list(soup.find_all('span')[4]))
  livenum = livenum.replace("['", "")
  livenum = livenum.replace(",", "")
  livenum = livenum.replace(" ']", "")

  return int(livenum)

#printing
def printing(total):
  print ("Date: ")
  print ("%02d/%02d/%04d" % (now.month, now.day, now.year))
  print ("Total:")
  print (total)
  print ("Iteration:")
  print (itera)
  print ("==============")

#initial print
printing(update())

#repeating print
while True:
  timer = timer - 0.01
  if timer <= 0:
    itera = itera + 1
    printing(update())
    timer = 60000.0
