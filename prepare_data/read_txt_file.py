import json
import random
import urllib
import os
import imghdr
import shutil

nb_sample = 1000

data = []
with open('nus_urls.txt') as f:
        for line in f:
                l = line.split()
                data.append(l)
f.close()
data.pop(0)

length = len(data)
shuf = [i for i in range(length)]
count = 0
index = 0

while count < nb_sample and index < length:
        try:
                if data[shuf[index]][3][-3:] != 'jpg':
                        index += 1
                        continue
                if count % 500 == 0:
                        print('%d nus-wide normal images have been downloaded... %d remaining...' % (count, nb_sample - count))
                if not os.path.exists('./normal'):
                    os.mkdir('./normal')
                p = os.path.join('./normal/', os.path.split(data[shuf[index]][3])[1])
                urllib.urlretrieve(data[shuf[index]][3], p)
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
