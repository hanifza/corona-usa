from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os

now = datetime.now()
#iterations
i = 1

#total live number fetcher (web scraper)
def update():
  page = requests.get('https://www.worldometers.info/coronavirus/country/us/')
  soup = BeautifulSoup(page.content, 'html.parser')
  cases = str(list(soup.find_all('span')[4]))
  cases = cases.replace('[\'', '')
  cases = cases.replace(',', '')
  cases = cases.replace(' \']', '')

  return int(cases)

def printing(total):
  #Clears the screen
  os.system('cls' if os.name == 'nt' else 'clear')
  print(f'''
    Date: {now.month}/{now.day}/{now.year}
    Total: {total}
    Iteration: {i}''')

#initial print
printing(update())

#repeating print
while True:
  printing(update())
  i += 1
  sleep(2)
