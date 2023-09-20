import requests
from bs4 import BeautifulSoup

import csv
url = "https://bleacherreport.com/articles/2151392-ranking-the-top-50-batsman-in-test-cricket-history-by-runs-scored-at-home"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

h2_elements = soup.find_all('h2')
rank_elements = soup.find_all('div', class_='slideData')
photographer_elements = soup.find_all('span', itemprop='citation', class_='credit')
player_names = []
ranks = []
photographer_names = []
for h2, rank, photographer in zip(h2_elements, rank_elements, photographer_elements):
    player_name = h2.text.strip()
    rank_text = rank.text.strip() 
    rank_number = rank_text.split()[0]
    photographer_name = photographer.text.strip() 

    player_names.append(player_name)
    ranks.append(rank_number)
    photographer_names.append(photographer_name)
with open('player_info.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Rank', 'Player Name', 'Photographer Name']) 
    for rank, name, photographer in zip(ranks, player_names, photographer_names):
        writer.writerow([rank, name, photographer])

print("Data has been written to 'player_info.csv'.")