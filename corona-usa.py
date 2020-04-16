from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os

#Web scraper
def get_cases():
    page = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    soup = BeautifulSoup(page.content, 'html.parser')
    cases = str(list(soup.find_all('span')[4]))
    #Removes unwanted chars
    for char in "[' ']":
        cases = cases.replace(char, '')
    return cases

i = 1
def print_cases(total):
    now = datetime.now()
    # Clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''Date (m/d/y): {now.month}/{now.day}/{now.year}
Total Cases: {total}
Iteration: {i}''')

#Waits 5 seconds between updates
while True:
    print_cases(get_cases())
    i += 1
    sleep(5)