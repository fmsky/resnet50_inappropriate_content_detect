import math, json, os, sys

import keras
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing import image


DATA_DIR = 'fine_tune_data'
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
VALID_DIR = os.path.join(DATA_DIR, 'validation')
SIZE = (224, 224)
BATCH_SIZE = 32


if __name__ == "__main__":
    num_train_samples = sum([len(files) for r, d, files in os.walk(TRAIN_DIR)])
    num_valid_samples = sum([len(files) for r, d, files in os.walk(VALID_DIR)])

    num_train_steps = math.floor(num_train_samples/BATCH_SIZE)
    num_valid_steps = math.floor(num_valid_samples/BATCH_SIZE)

    gen = keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True, vertical_flip=True, rotation_range=40, zoom_range=0.2, width_shift_range=0.2, height_shift_range=0.2)
    val_gen = keras.preprocessing.image.ImageDataGenerator(horizontal_flip=True, vertical_flip=True, rotation_range=40, zoom_range=0.2, width_shift_range=0.2, height_shift_range=0.2)

    batches = gen.flow_from_directory(TRAIN_DIR, target_size=SIZE, class_mode='binary', shuffle=True, batch_size=BATCH_SIZE)
    val_batches = val_gen.flow_from_directory(VALID_DIR, target_size=SIZE, class_mode='binary', shuffle=True, batch_size=BATCH_SIZE)

    model = keras.applications.resnet50.ResNet50()

    classes = list(iter(batches.class_indices))
    model.layers.pop()
    for layer in model.layers:
        layer.trainable=False
    last = model.layers[-1].output
    #x = Dense(len(classes), activation="softmax")(last)
    x = Dense(1, activation="sigmoid")(last)
    finetuned_model = Model(model.input, x)
    #finetuned_model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    finetuned_model.compile(optimizer=Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
    for c in batches.class_indices:
        classes[batches.class_indices[c]] = c
    finetuned_model.classes = classes

    early_stopping = EarlyStopping(patience=10)
    checkpointer = ModelCheckpoint('./data/resnet50_best.h5', verbose=1, save_best_only=True)

    finetuned_model.fit_generator(batches, steps_per_epoch=num_train_steps, epochs=1000, callbacks=[early_stopping, checkpointer], validation_data=val_batches, validation_steps=num_valid_steps)
    finetuned_model.save('resnet50_final.h5')
