import pandas as pd
import os
import urllib

table = {'violence':'/m/0chbx', 'cartoon':'/m/0215n', 'comics':'/m/012h24', 'medical':'/m/02xht4g'}

keyword = 'violence'
value = table[keyword]

df = pd.read_csv('train_labels.csv')
train = df[df['LabelName'] == value]
train_id = train['ImageID'].tolist()

df = pd.read_csv('train_images.csv')
for iden in train_id:
	row = df[df['ImageID'] == iden]
	url = row['Thumbnail300KURL'].tolist()
	try:
		print('Downloading image ', iden, ' from thumbnail url...')
		urllib.urlretrieve(url[0], os.path.join(keyword, os.path.split(url[0])[1]))
	except Exception as e:
		print('Failed to download image ', iden, ' from thumbnail url, trying to download from original url')
		try:
			url = row['OriginalURL'].tolist()
			urllib.urlretrieve(url[0], os.path.join(keyword, os.path.split(url[0])[1]))
		except Exception as e:
			print('Failed to download image ', iden, ' from orginal url')
			continue

df = pd.read_csv('val_labels.csv')
val = df[df['LabelName'] == value]
val_id = val['ImageID'].tolist()

df = pd.read_csv('val_images.csv')
for iden in val_id:
	row = df[df['ImageID'] == iden]
	url = row['Thumbnail300KURL'].tolist()
	try:
		print('Downloading image ', iden, ' from thumbnail url...')
		urllib.urlretrieve(url[0], os.path.join(keyword, os.path.split(url[0])[1]))
	except Exception as e:
		print('Failed to download image ', iden, ' from thumbnail url, trying to download from original url')
		try:
			url = row['OriginalURL'].tolist()
			urllib.urlretrieve(url[0], os.path.join(keyword, os.path.split(url[0])[1]))
		except Exception as e:
			print('Failed to download image ', iden, ' from orginal url')
			continue
