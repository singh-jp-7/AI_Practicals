import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import numpy as np 


extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'
  
SHORT_HEADERS = ['SNo', 'State','Total-Confirmed','Cured','Death'] 
  
response = requests.get(URL).content 
soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th')) 
  
stats = [] 
all_rows = soup.find_all('tr') 
  
for row in all_rows: 
    stat = extract_contents(row.find_all('td')) 
    if stat: 
        if len(stat) == 5: 
            stat = ['', *stat] 
            stats.append(stat) 
        elif len(stat) == 6: 
            stats.append(stat) 


objects = [] 
for row in stats : 
    objects.append(row[1])  
    
  
y_pos = np.arange(len(objects)) 
  
performance = [] 
deaths = []
cured = []
for row in stats : 
    performance.append(int(row[3])) 
    deaths.append(int(row[5]))
    cured.append(int(row[4]))
    total_cases = sum(performance)
    total_deaths = sum(deaths)
    total_cured = sum(cured)
  
table = tabulate(stats, headers=SHORT_HEADERS) 
print(table) 
print()
print("-"*80)
print()
print("Total cases : ",total_cases)
print("Total cured :",total_cured)
print("Total deaths :",total_deaths)  
