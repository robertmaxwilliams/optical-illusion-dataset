# downloads every image in the moillusions_data.json file
# and stores them in 'data' folder, which is in .gitignore
# with filenames as index in the json file

import json
import requests
import os
import shutil
import multiprocessing

if not os.path.exists('data/'):
    os.makedirs('data/')

def download_image(image_dict):
	index = image_dict['index']
	url = image_dict['img_src']
	
	# fix broken urls
	if url[0] == '/':
		url = 'https:' + url

	# name files with left padded n 5 digit number and extension
	extension = url.split('.')[-1]
	# this happens when no extention is supplied in url
	if len(extension) > 4:
		extension = ''
	filename = str(index).zfill(5) + '.' + extension

	# quit if it is already downloaded
	if os.path.isfile('data/'+filename):
#		print('have ', filename)
		return

	try:
		response = requests.get(url, stream=True)
	except requests.exceptions.SSLError:
		print('failed', image_dict)
		return

	print(filename)
	with open('data/'+filename, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response

# load json file
moillusions = json.load(open('moillusions_data.json'))
# add 'index' to each entry
for i, data in enumerate(moillusions):
	data['index'] = i

p = multiprocessing.Pool(10)
p.map(download_image, moillusions)
