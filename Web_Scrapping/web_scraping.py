import urllib2
from bs4 import BeautifulSoup
import json
import pandas as pd 

print(">>>> Fwetching the data from the url provided...")

url='https://www.yellowpages.com/search?search_terms=coffee+shop&geo_location_terms=Irving%2C+TX'
response = urllib2.urlopen(url)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

# Optional # removes script and style tags from soup
# for script in soup(["script", "style"]):
#     script.extract()

results = []

print(">>>> Started scrapping the data for the results...")

for div in (soup.find_all('div',{ "class" : "info" })[1:]):
	
	shop_name = div.h2.get_text().split('.')[1].strip()

	streetAddress = div.find('p', {'class': "adr"}).find('span', {'itemprop': 'streetAddress'}).get_text()
	addressLocality = (div.find('p', {'class': "adr"}).find('span', {'itemprop': 'addressLocality'}).get_text()).split(',')[0]
	addressRegion = div.find('p', {'class': "adr"}).find('span', {'itemprop': 'addressRegion'}).get_text()
	postalCode = div.find('p', {'class': "adr"}).find('span', {'itemprop': 'postalCode'}).get_text()

	address = streetAddress + ", " + addressLocality + ", " + addressRegion + " " + postalCode

	phone  = div.find('div', {'class': "phone"}).get_text()

	#temp dictionay for storing data
	data = {}
	data['phone'] = phone
	data['address'] = address.decode('unicode_escape').encode('ascii','ignore')
	data['shop_name'] = shop_name
	
	# external dict for for stroing all data
	results.append(data)

print(">>>> Converting the results into json...")

# converting dict to json
json_data = json.dumps(results)

print(">>>> Creating DataFrame for the results...")

# Converting the results into a dataframe
df = pd.DataFrame.from_records(results)

print(">>>> Writing results to a csv file")

# converting to a csv file
df.to_csv('top_30_search_results.csv', mode='w', encoding='utf-8')