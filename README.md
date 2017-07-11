# resnet50_inappropriate_content_detect
Fine-tuned resnet50 model in Keras to detect images content such as: adult, violence, cartoon, medical and spoof

## Configuration
Hardware: AWS EC2 p2.xlarge

OS: Linux/Unix, Amazon Linux 2016.09

Software: Keras

## Dataset
1. dataset of adult image metadata in this repository: 
[pornhub database](https://github.com/ZixuanLiang/hub-db "pornhub database")

2. dataset of violence/cartoon image metadata in google open images dataset (scrap images with label names): 
[Google Open Images](https://github.com/openimages/dataset "Google Open Images")

3. dataset of normal image metadata in NUS-WIDE dataset:
[NUS-WIDE images urls](http://dl.nextcenter.org/public/nuswide/NUS-WIDE-urls.rar "NUS-WIDE images urls")

## Training
run resnet50_train.py

Description: Use pretrained model [ResNet50](https://keras.io/applications/#resnet50 "ResNet50") in Keras. It has weights pretrained on ImageNet. Then replace the top layer. To fine-tune this model, only train the top layer and set the rest layers to be untrainable. Because I only use no more than 30000 images to train each model, I utilize data augmentation in ImageDataGenerator. For the optimizer I use Adam.

## Result
For different models to detect different kinds of content, they are tested with independent data set(roughly 2000 images) and achieve accuracy as below:

adult: 93%

violence: 97%

cartoon: 94%.

disgusting: ongoing.

## Improve:
While the models achieve fairly good accuracy, they have potential for improvement. There are a few possible ways. 

Collect more precisely labeled images. Because I only collected roughly 30000 images for each model (train, validation and test) from particular websites/open dataset/search engine and I didn't check the correctness of all samples, training data is inevitably somehow noisy. Collecting more images means more training time and manually checking tens of thousands of images by myself is impratical. 

Data augmentation. To make full use of limited number of images, we can use more aggresive data augmentation in ImageDataGenerator. We can explore better augmentation strategy by setting different values for different arguments in this generator. 

Fine tune more convolutional layers in ResNet50 model rather than only the top layer. 

Add regularization (weight decay) to defeat overfitting. They allow to apply penalties on layer parameters or layer activity during optimization. 

Adjust other arguments. For the optimizer I user Adam, which is considered one of the best adaptive learning rate methods by far with fast convergence. We can try other options such as SGD + Nesterov momentum. We can decay the learning rate along with training in the optimizer. Initial learning rate also affects the final performance. Ensemble independent models can also lead to better performance. 
