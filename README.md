# resnet50_inappropriate_content_detect
Fine-tuned resnet50 model in Keras to detect images content such as: adult, violence, cartoon, medical and spoof

## Configuration:
Hardware: AWS EC2 p2.xlarge

OS: Linux/Unix, Amazon Linux 2016.09

Software: Keras

## Dataset:
1. dataset of adult image metadata in this repository: 
[pornhub database](https://github.com/ZixuanLiang/hub-db "pornhub database")

2. dataset of violence image metadata in google open images dataset (scrap images with label name "violence"): 
[Google Open Images](https://github.com/openimages/dataset "Google Open Images")

3. dataset of normal image metadata in NUS-WIDE dataset:
[NUS-WIDE images urls](http://dl.nextcenter.org/public/nuswide/NUS-WIDE-urls.rar "NUS-WIDE images urls")

## Training:
run resnet50_train.py

Description: Use pretrained model [ResNet50](https://keras.io/applications/#resnet50 "ResNet50") in Keras. It has weights pretrained on ImageNet. Then replace the top layer. To fine-tune this model, only train the top layer and set the rest layers to be untrainable. Because I only use no more than 30000 images to train each model, I utilize data augmentation in ImageDataGenerator. For the optimizer I use Adam.

## Result:
For different models to detect different kinds of content, they are tested with independent data set and achieve accuracy as below:

adult: 93%

violence: 97%

cartoon: 94%.

medical: ongoing.

spoof: ongoing.
