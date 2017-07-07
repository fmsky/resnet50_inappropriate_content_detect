import shutil
import os
from random import shuffle

folders = ['porn','normal']
nb_of_sample = 14000
nb_train = 10000
nb_val = 4000

pwd = os.getcwd()

for folder in folders:
    train_path = os.path.join(pwd, 'fine_tune_data/train', folder)
    val_path = os.path.join(pwd, 'fine_tune_data/validation', folder)
    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(val_path):
        os.makedirs(val_path)
    images = os.listdir(os.path.join(pwd, folder))
    length = len(images)
    shuf = [i for i in range(length)]
    shuffle(shuf)
    for i in range(nb_of_sample):
        file_path = os.path.join(pwd, folder, images[shuf[i]])
        if i < nb_train:
            shutil.copyfile(file_path, os.path.join(train_path, images[shuf[i]]))
        else:
            shutil.copyfile(file_path, os.path.join(val_path, images[shuf[i]]))
