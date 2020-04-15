import requests
from bs4 import BeautifulSoup
from datetime import datetime

#variables
now = datetime.now()
timer = 60000.0
i = 1

#total live number fetcher (web scraper)
def update():
  page = requests.get("https://www.worldometers.info/coronavirus/country/us/")

  soup = BeautifulSoup(page.content, 'html.parser')

  live_num = str(list(soup.find_all('span')[4]))
  live_num = live_num.replace("['", "")
  live_num = live_num.replace(",", "")
  live_num = live_num.replace(" ']", "")

  return int(live_num)

#printing
def printing(total):
  print(f'''
    Date: {now.month}/{now.day}/{now.year}
    Total: {total}
    Iteration: {i}''')

#initial print
printing(update())

#repeating print
while True:
  timer = timer - 0.01
  if timer <= 0:
    i = i + 1
    printing(update())
    timer = 60000.0
