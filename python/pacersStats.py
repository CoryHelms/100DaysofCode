import requests, bs4

page = requests.get('https://www.basketball-reference.com/teams/IND/2022.html')
soup = bs4.BeautifulSoup(page.text, 'html.parser')

stats = soup.find_all('table', attrs={'id':'per_game'})


