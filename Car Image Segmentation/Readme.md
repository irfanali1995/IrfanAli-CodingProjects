# Image Segmentation using U-Net Model

## Overview
This project aims to perform image segmentation of cars using the U-Net model. Image segmentation is the task of dividing an image into meaningful segments or regions. In this project, we focus on segmenting cars from images by training a U-Net neural network on a dataset of car images and their corresponding masks.

## Code Overview
### Image Pre-processing
Before feeding the data into the neural network, the images in the training and test sets, along with their corresponding masks, are individually resized to a standard size of 128x128x3. The masks are also converted into binary images using Otsu’s method. The processed images and masks are then saved into indexed matrices.

### U-Net Network
#### Compiling the Model
The U-Net model is compiled with the following configurations:
- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Metrics: Accuracy

#### Number of Epochs and Early Stopping
The model is trained for 50 epochs. However, to avoid overfitting and achieve early stopping, a callback is utilized to stop training if there is no improvement for two additional epochs.

#### Validation Split
A validation split of 10% is used to evaluate the model's performance during training.

### Post Training & Compiling
After training the model, the best weights are saved. The trained model is then used to make predictions on both the training and test images. A random set of 50 sequential training images, along with their corresponding training masks and predicted masks, is displayed to visualize the results.

Similarly, a random set of 50 sequential test images with their corresponding predicted masks is displayed to visualize the prediction results for the test set.

## Results
Training Results Comparison: 
 ![image](https://github.com/irfanali1995/Masters_Robotics-/assets/75564524/64fbdd28-3ab4-4be2-bf19-58180c5db16e)

Test Results:
 ![image](https://github.com/irfanali1995/Masters_Robotics-/assets/75564524/16e60b17-1ef5-4b07-9176-b6de1f87496e)

## Pros and Cons of U-Net for using Image Segmentation of Car
   Pros: 
      - Flexible and can be used for any rational image masking task
      - High accuracy (given proper training, dataset, and training time) 
      - Succeeds to achieve very good performances on different biomedical segmentation applications
   Cons:
      - Larger images need high GPU memory
      - Takes significant amount of time to train 
      - Pre-trained models not widely available

## Dependencies
- Python (>= 3.6)
- TensorFlow (>= 2.0)


**<span style="color:red;">Note:</span>** If you are interested in using or contributing to this project, please contact for permission or further information.


