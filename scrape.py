# Import libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Collect first page of artists’ list
driver = webdriver.Firefox()
driver.get('https://www.nga.gov/collection/artists.html?const_startLetter=z&pageNumber=1&lastFacet=const_startLetter')

# page = requests.get('https://www.nga.gov/collection/artists.html?const_startLetter=z&pageNumber=1&lastFacet=const_startLetter')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='collectionsResultListings')
# print(artist_name_list)

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')
# print (artist_name_list_items)
# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())
