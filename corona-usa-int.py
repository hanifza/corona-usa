from time import sleep
from bs4 import BeautifulSoup
import requests

#total live number fetcher (web scraper)
def update():
  page = requests.get('https://www.worldometers.info/coronavirus/country/us/')
  soup = BeautifulSoup(page.content, 'html.parser') #gathers HTML link
  cases = str(list(soup.find_all('span')[4])) #HTML line w/ total
  cases = cases.replace('[\'', '')
  cases = cases.replace(',', '')
  cases = cases.replace(' \']', '')

  return int(cases)


#repeating update
while True:
  update()
  sleep(60)
