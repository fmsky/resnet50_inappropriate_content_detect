from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import shutil

file_path = './resnet50_final.h5'
test_data_dir = './test'

batch_size = 200
nb_samples = 2000
SIZE = (224, 224)

model = load_model(file_path)

test_datagen = ImageDataGenerator()

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=SIZE,
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False)

result = model.predict_generator(test_generator, nb_samples // batch_size)

correct_normal = 0
correct_porn = 0
wrong_normal = []
wrong_porn = []

for i, n in enumerate(test_generator.filenames):
    if n.startswith("normal") and result[i][0] <= 0.9:
        correct_normal += 1
    elif n.startswith("porn") and result[i][0] > 0.9:
        correct_porn += 1
    elif n.startswith("normal") and result[i][0] > 0.9:
    	wrong_normal.append(result[i][0])
        shutil.copyfile('./test/normal/'+n[6:], './misclasify_test/normal/'+str(result[i][0])+'.jpg')
    elif n.startswith("porn") and result[i][0] <= 0.9:
        wrong_porn.append(result[i][0])
        shutil.copyfile('./test/porn/'+n[4:], './misclasify_test/porn/'+str(result[i][0])+'.jpg')
print('correct normal: ', correct_normal, ' correct porn: ', correct_porn, ' total: ', nb_samples)
print('wrong normal')
print(wrong_normal)
print('wrong porn')
print(wrong_porn)
    
