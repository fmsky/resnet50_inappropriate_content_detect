# resnet50_nsfw
Fine-tuned resnet50 model in Keras to detect images content such as: adult, violence, cartoon, medical and spoof

## Prerequisite:
Keras
Linux machine with GPU

## Dataset:
1. dataset of adult image metadata in this repository: 
[pornhub database](https://github.com/ZixuanLiang/hub-db "pornhub database")
2. dataset of violence image metadata in google open images dataset (scrap images with label name "violence"): 
[Google Open Images](https://github.com/openimages/dataset "Google Open Images")
3. dataset of normal image metadata in NUS-WIDE dataset:
[NUS-WIDE images urls](http://dl.nextcenter.org/public/nuswide/NUS-WIDE-urls.rar "NUS-WIDE images urls")

## Training:
run resnet50_train.py

Description: Use pretrained model [ResNet50](https://keras.io/applications/#resnet50 "ResNet50") in
Keras. It has weights pretrained on ImageNet. Then replace the top layer. To fine-tune this model, only train the top layer and
set the rest layers to be untrainable. Because I only use no more than 30000 images to train each model, I utilize data augmentation
in ImageDataGenerator. For the optimizer I use Adam.

## Result:
For adult content detect model it achieves 93% accuracy on test set.

For violence content detect model it achieves 96.7% accuracy on test set.

Cartoon model: ongoing.

Medical model: ongoing.

Spoof model: ongoing.
