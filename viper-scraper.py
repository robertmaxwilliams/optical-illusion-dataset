# web scraper to scrape a section of viper 
# http://viperlib.york.ac.uk/
# for thumbnail images and store the URLs in JSON format. Mmmm JSON....
 
from bs4 import BeautifulSoup

import requests
import time
import json


start_pages = ['http://viperlib.york.ac.uk/areas/16-lightness-brightness/contributions?page=*&sort=by_title',
			'http://viperlib.york.ac.uk/areas/12-colour/contributions?page=*&sort=by_title',
			'http://viperlib.york.ac.uk/areas/18-depth/contributions?page=*&sort=by_title',
			'http://viperlib.york.ac.uk/areas/25-faces/contributions?page=*&sort=by_title',
			'http://viperlib.york.ac.uk/areas/20-illusions/contributions?page=*&sort=by_title',
			'http://viperlib.york.ac.uk/areas/16-lightness-brightness/contributions?page=*&sort=by_title',
			'http://viperlib.york.ac.uk/areas/13-motion/contributions?page=*&sort=by_title',
			'http://viperlib.york.ac.uk/areas/14-spatial-vision/contributions?page=*&sort=by_title',]

def scrape_images_and_text(url, category):
	print(url)
	# obtain 'soup' which lets us find parts in the page
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')

	# for each div class=contribution, collect data
	# package into dict, and yield
	images = list()
	for sample in soup.find_all('div', {'class':'contribution'}):
		image = sample.find('img')
		image_dict = {'url':image.get('src'),
					'title':image.get('alt'),
					'page_url':sample.find('a').get('href'),
					'category':category,
					'description':tuple(sample.find_all('p'))[-1].text}
		yield image_dict
		print('\t', image_dict['title'])
		print('\t\t', image_dict)

def write_to_json(data):
	with open('data.json', 'w') as json_file:
		json_file.write(json.dumps(data))

images = list()
for base_url in start_pages:
	category = base_url.split('/')[4]
	i = 1
	while True:
		url = base_url.replace('*', str(i))
		start_len = len(images)
		images += scrape_images_and_text(url, category)
		if (start_len == len(images)):
			break
		i+=1
	write_to_json(images)
