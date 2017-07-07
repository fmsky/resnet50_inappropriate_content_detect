import os
import shutil

files = os.listdir('.')
count = 0
for f in files:
    if f.endswith('?zz=1'):
        shutil.move(f, f[:-5])
        count += 1
print(count)
