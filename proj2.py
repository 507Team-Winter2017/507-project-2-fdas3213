#proj2.py
import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
baseurl = 'http://www.nytimes.com'
html = urllib.request.urlopen(baseurl)
soup = BeautifulSoup(html, 'html.parser')
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
mi_html = urllib.request.urlopen(mi_url)
mi_soup = BeautifulSoup(mi_html, 'html.parser')
most_read = []
for heading in mi_soup.find_all('li'):
	for a in heading.find_all('a'):
		text = a.get_text()
		if len(text) > 15:
			most_read.append(text)

for ind in range(5):
	print(most_read[ind])



#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

img_url = 'http://newmantaylor.com/gallery.html'
img_html = urllib.request.urlopen(img_url)
img_soup = BeautifulSoup(img_html, 'html.parser')
img_list = []

for img in img_soup.find_all('img'):
	if img.get('alt'):
		word = img.get('alt')
	else:
		word = None
	img_list.append(word)

for ind in range(len(img_list)):
	print(img_list[ind])



'''#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here'''
