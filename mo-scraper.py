# Web scraper to collect all illusions from the site
# https://www.moillusions.com/
# they also have other content but we don't want that
# getting the tags (categories) would also be nice

from bs4 import BeautifulSoup

import requests
import time
import json

start_url = 'https://www.moillusions.com/one-two-face-illusion/'
url = start_url
outfile_name = str(time.time())

# image_list is a list of dicts with  url, img_src, alt_text, categories for each image
image_list = list()

while True:
	try:
		print(url)
		r  = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data, 'lxml')

		# collect all categories
		categories = list()
		for link in soup.find_all('a', {'rel':'category tag'}):
			categories.append(link.text)

		# get all image links, except avatar images
		for link in soup.find_all('img'):
			img_src = link.get('src')

			# easy way to filter out avatar images
			if 'https://secure.gravatar.com/avatar/' in img_src:
				continue

			alt_text = link.get('alt')
			image_data = {'url':url, 'img_src':img_src, 'alt_text':alt_text, 'categories':categories[:]} 
			image_list.append(image_data)

			print('\t', img_src)

			# every 20 images sampled, write a backup and print how it's going
			if (len(image_list) % 20 == 0): 
				print("pages scraped:", len(image_list))
				with open('.backup_' + str(len(image_list)) + '.json', 'w') as backup_file:
					backup_file.write(json.dumps(image_list))



		# get the prev button. There should only be one
		new_url = None
		for link in soup.find_all('a', {'rel':'prev'}):
			new_url = link.get('href')

		# if not "prev" url is supplied, exit the program. Either failure state or end of pages.
		if new_url == None:
			print("failed to get next url, ending")
			break
		if new_url == start_url:
			print("looped back to start, ending")
			break
		else:
			url = new_url

		# sleep so we don't get booted
		#eh, lets not and say we did time.sleep(0.5)

	# I needed to save when there is an error. I hope this is the right way to do it!
	except Exception as err:
		print('there has been as issue. writing json file and aborting')
		with open('failure_backup.json', 'w') as backup_file:
			backup_file.write(json.dumps(image_list))
		raise err

# after we're done or failed or blocked, write to data.json
with open('data.json', 'w') as json_file:
	json_file.write(json.dumps(image_list))
