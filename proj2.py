#proj2.py
import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup
import re


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')


nytimes_url = 'http://www.nytimes.com'
def generate_soup(url):
	html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html, 'html.parser')
	return soup

soup = generate_soup(nytimes_url)
story_heading = []

for heading in soup.find_all(class_='story-heading'):
	if heading not in story_heading:
		if heading.a:
			story_heading.append(heading.a.text.replace('\n', " ").strip())
		else:
			story_heading.append(heading.contents[0].strip())

for ind in range(10):
	print(story_heading[ind])


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

mi_url = 'https://www.michigandaily.com'
mi_soup = generate_soup(mi_url)

for heading in mi_soup.find_all('li'):
	for a in heading.find_all('a'):
		text = a.get_text()
		if len(text) > 15:
			print(text)


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

img_url = 'http://newmantaylor.com/gallery.html'
img_soup = generate_soup(img_url)

for img in img_soup.find_all('img'):
	word = img.get('alt') if img.get('alt') else 'No alternative text provided!'
	print(word)



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")
pattern = '.*@umich.edu'
contact = []

def get_soup(url):
	r = urllib.request.Request(url, None, {'User-Agent': 'SI_CLASS'})
	html = urllib.request.urlopen(r)
	soup = BeautifulSoup(html, 'html.parser')
	return soup

email_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
um_url = 'https://www.si.umich.edu'

email_soup = get_soup(email_url)

def get_url(soup):
	for alt in soup.find_all('a'):
		if alt.get_text() == 'Contact Details':
			hr = alt.get('href')
			url = um_url + hr
			contact.append(url)

get_url(email_soup)

def next_page(soup):
	for alt in soup.find_all('a', title = 'Go to next page'):
		page = um_url + alt.get('href')
		soup = get_soup(page)
	return soup

def add_soup(soup):
	for i in range(5):
		num_soup = next_page(soup)
		soup = num_soup
		get_url(num_soup)

add_soup(email_soup)

for url in contact:
	ind_soup = get_soup(url)
	for di in ind_soup.find_all('div', class_='field-item even'):
		for alt in di.find_all('a'):
			if re.search(pattern, alt.get_text()):
				print(alt.get_text())



