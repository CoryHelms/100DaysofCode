import pandas as pd
import requests
from bs4 import BeautifulSoup

# Wikipedia (https://en.wikipedia.org/wiki/List_of_current_NCAA_Division_I_FBS_football_coaches)
# Pull College Football Coach Names
# Fetch Overall Coaching Record
# Write function to calculate win percentage from overall record

#get response in HTML
url="https://en.wikipedia.org/wiki/List_of_current_NCAA_Division_I_FBS_football_coaches"
tableClass = "wikitable sortable"
response = requests.get(url)
##print(response.status_code)

#parse HTML
soup = BeautifulSoup(response.text, 'html.parser')
coachTable = soup.find('table', {'class':'wikitable'})
tableBody = coachTable.find('tbody')

##rows = tableBody.findAll('tr')
##for row in rows:
##    data = row.findAll('td')
##    print(data)
