import json
import random
import urllib
import os
import imghdr
import shutil

nb_sample = 1000

data = []
with open('images_1.json') as f:
	for line in f:
		data.append(json.loads(line))
f.close()
with open('images_2.json') as f:
	for line in f:
		data.append(json.loads(line))
f.close()
shuf = [i for i in range(len(data))]
count = 0
index = 0
while count < nb_sample and index < len(data):
	try:
		if data[shuf[index]]['uri'][-3:] != 'jpg':
			index += 1
			continue
		if count % 500 == 0:
			print('%d porn images have been downloaded... %d remaining...' % (count, nb_sample - count))
		if not os.path.exists('./porn'):
          		os.mkdir('./porn')
          	p = os.path.join('./porn/', os.path.split(data[shuf[index]]['uri'])[1])
		urllib.urlretrieve(data[shuf[index]]['uri'], p)
		if imghdr.what(p) == 'jpeg':
			count += 1
		else:
			shutil.remove(p)
		index += 1
	except Exception as e:
		index += 1
		continue

if count == nb_sample:
	print('downloaded all images needed \n')
else:
	print('%d images not downloaded' & (nb_sample - count))

		
