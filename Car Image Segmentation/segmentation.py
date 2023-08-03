Python Code:
######################################################################
import tensorflow as tf
from tensorflow import keras import os
import numpy as np
import random
from tqdm import tqdm # for progress bar
from skimage import io
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage import img_as_ubyte #use to convert output images to ubyte import cv2
import matplotlib.pyplot as plt import datetime
#seed for random selection of images displayed seed = 42
np.random.seed = seed
#Image scale for input/output from U-Net network IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_CHANNELS = 3
#File path of images
TRAIN_PATH = 'E:/Users/Owner/Documents/cvpr-2018-autonomous-driving/train_color-10000' TRAIN_MASK_PATH = 'E:/Users/Owner/Documents/cvpr-2018-autonomous-driving/train_label' TEST_PATH = 'E:/Users/Owner/Documents/cvpr-2018-autonomous-driving/test' #Find files only within provided file path
train_ids = next(os.walk(TRAIN_PATH))[2]
train_mask_ids = next(os.walk(TRAIN_MASK_PATH))[2]
test_ids = next(os.walk(TEST_PATH))[2]
 X_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8) #create input matrix with zeros to set size we want
Y_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, 1))#create expected output matrix with false values to set size of matrix we want
mask = np.zeros((IMG_HEIGHT, IMG_WIDTH,1))
# In[ ]:
print('Resizing training images and masks')
for n, id_ in tqdm(enumerate(train_ids), total=len(train_ids)): #Cycle through all the images using enumerate, counting the image files and outputting the file id
path = TRAIN_PATH + '/' + id_ #create the full file path to the image by adding the image id
img = imread(path)[:,:,:IMG_CHANNELS] #read the .jpg training image
img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True) #resize the image for the U-Net neural network
X_train[n] = img #Fill empty X_train with values from img
#for mask_file in next(os.walk(path + '/masks/'))[2]:
mask_path = TRAIN_MASK_PATH + '/' + id_[:-4] #create the full file path to the image by adding the image id
# print(mask_path)
mask = cv2.imread(mask_path + '_instanceIds' + '.png')#read the .png training image mask
#Convert masked image into a gray image
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
#Utilize Otsu’s method to make the image binary
_, mask = cv2.threshold(mask,125,255,cv2.THRESH_BINARY) #Resize the image for the U-Net neural network
Y_train[n] = resize(mask, (IMG_HEIGHT, IMG_WIDTH, 1))
# Test images processing
# Size variable to U-Net input size
X_test = np.zeros((len(test_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
sizes_test = []
print('Resizing test images')
for n, id_ in tqdm(enumerate(test_ids), total=len(test_ids)): #1917 test images

 path = TEST_PATH + '/' + id_ #create the full file path to the image by adding the image id
img = imread(path)[:,:,:IMG_CHANNELS]#read the .png test image sizes_test.append([img.shape[0], img.shape[1]])
img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True) X_test[n] = img
print('Done!')
# In[ ]:
inputs = tf.keras.layers.Input((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)) s = tf.keras.layers.Lambda(lambda x: x / 255)(inputs)
#Contraction path
c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(s)
c1 = tf.keras.layers.Dropout(0.1)(c1)
c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c1)
p1 = tf.keras.layers.MaxPooling2D((2, 2))(c1)
c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p1)
c2 = tf.keras.layers.Dropout(0.1)(c2)
c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c2)
p2 = tf.keras.layers.MaxPooling2D((2, 2))(c2)
c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p2)
c3 = tf.keras.layers.Dropout(0.2)(c3)
c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c3)
p3 = tf.keras.layers.MaxPooling2D((2, 2))(c3)
c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p3)
c4 = tf.keras.layers.Dropout(0.2)(c4)

 c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c4)
p4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(c4)
c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p4)
c5 = tf.keras.layers.Dropout(0.3)(c5)
c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c5)
#Expansive path
u6 = tf.keras.layers.Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c5) u6 = tf.keras.layers.concatenate([u6, c4])
c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
c6 = tf.keras.layers.Dropout(0.2)(c6)
c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)
u7 = tf.keras.layers.Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c6) u7 = tf.keras.layers.concatenate([u7, c3])
c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
c7 = tf.keras.layers.Dropout(0.2)(c7)
c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)
u8 = tf.keras.layers.Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c7) u8 = tf.keras.layers.concatenate([u8, c2])
c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
c8 = tf.keras.layers.Dropout(0.1)(c8)
c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)
u9 = tf.keras.layers.Conv2DTranspose(16, (2, 2), strides=(2, 2), padding='same')(c8) u9 = tf.keras.layers.concatenate([u9, c1], axis=3)
c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
c9 = tf.keras.layers.Dropout(0.1)(c9)
c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)

 outputs = tf.keras.layers.Conv2D(1, (1, 1), activation='sigmoid')(c9) model = tf.keras.Model(inputs=[inputs], outputs=[outputs])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) model.summary()
#checkpoint
checkpointer = tf.keras.callbacks.ModelCheckpoint('model_for_vehicle_segmentation', verbose = 1, save_best_only = True) # Set to save best model
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") #Create distinct file path to save results
callbacks = [tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)] #Send training to tensorboard
# Set validation split, batch size, and number of epochs model.fit(X_train,Y_train, validation_split = 0.1, batch_size=16, epochs=50, callbacks=[callbacks])
# In[ ]:
#Save model model.save('vehiclesegment_test.h5')
# In[ ]:
#Extract predictions for training images and test images
preds_train = model.predict(X_train[:int(X_train.shape[0]*0.9)], verbose=1) preds_val = model.predict(X_train[int(X_train.shape[0]*0.9):], verbose=1) preds_test = model.predict(X_test, verbose=1)
#Set prediction values to 0 or 1
preds_train_t = (preds_train > 0.5).astype(np.uint8) preds_val_t = (preds_val > 0.5).astype(np.uint8) preds_test_t = (preds_test > 0.5).astype(np.uint8)

# In[ ]:
# Select a random training image index out of all training images ix = random.randint(1, (len(preds_train_t)-50))
print('ix = ', ix)
#Grab the indexed image and pull the next 50 in sequence for j in range(ix,ix+50):
print('j = ', j)
imshow(X_train[j]) #Display input training image
plt.show()
imshow(Y_train[j], cmap='gray') #Display training mask image
plt.show()
rand_in_train_image = img_as_ubyte(X_train[j]) imshow(preds_train_t[j].reshape(128,128), cmap='gray') #Display model prediction of
training image
plt.show()
# Select a random test image index out of all test images iy = random.randint(1, (len(preds_test_t)-50))
print('iy = ', iy)
#Grab the indexed image and pull the next 50 in sequence for k in range(iy,iy+50):
print('k = ', k)
imshow(preds_test[k].reshape(128,128), cmap='gray') #Display input test image plt.show()
imshow(X_test[k], cmap = 'gray') #Display model prediction of training image plt.show()
