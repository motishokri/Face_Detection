# -*- coding: utf-8 -*-
"""Face Detection in Images with Python using OpenCV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pH5T_thtvR6M-JVNxj51FJYboV3ytsBI

# What is Face Detection?

Face detection is the process of automatically identifying and locating human faces in images or videos. It involves analyzing visual input to determine the presence and location of facial features.

Since human faces exhibit various shapes, sizes, and appearances, face detection models require extensive training on diverse datasets to achieve accurate results. The training data should encompass individuals from different backgrounds, genders, and cultures to ensure the model's inclusivity and effectiveness.

To handle real-world scenarios, these algorithms need to be exposed to numerous training samples with varying lighting conditions, angles, and orientations to generalize well.

Developing an accurate face detection model from scratch can be a challenging and time-consuming task, as it demands extensive data preparation and training. However, there are pre-trained models available, like the ones provided by the OpenCV library. OpenCV employs a machine learning technique called Haar cascades, which allows it to efficiently identify objects, including faces, in visual data.

By utilizing pre-trained models, developers can save time and effort while still benefiting from robust face detection capabilities in their applications.

#Step 1: Import the OpenCV Package

Now, let’s import OpenCV and enter the input image path with the following lines of code:
"""

from matplotlib import pyplot as plt
import cv2

"""#Step 2: Read the Image

"""

img = cv2.imread("drive/MyDrive/nasa.jpg")

"""This will load the image from the specified file path and return it in the form of a Numpy array.

Let’s print the dimensions of this array:
"""

img.shape

"""Notice that this is a 3-dimensional array. The array’s values represent the picture’s height, width, and channels respectively. Since this is a color image, there are three channels used to depict it - blue, green, and red (BGR).

Note that while the conventional sequence used to represent images is RGB (Red, Blue, Green), the OpenCV library uses the opposite layout (Blue, Green, Red).

#Step 3: Convert the Image to BGR

To display the image with the detected faces, we first need to convert the image from the BGR format to RGB:
"""

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""#Step 4: Load the Classifier

Let’s load the pre-trained Haar model1 classifier that is built into OpenCV:
"""

model = cv2.CascadeClassifier("drive/MyDrive/model1.xml")

"""#Step 5: Perform the Face Detection

We can now perform face detection on the BGR image using the classifier we just loaded:
"""

faces = model.detectMultiScale(img, 1.1 ,4)

"""1. detectMultiScale():
The detectMultiScale() method is used to identify faces of different sizes in the input image.

2. img:
The first parameter in this method is called img, which is the grayscale image we created previously.

3. scaleFactor:
The second parameter in this method is called scaleFactor, This parameter is used to scale down the size of the input image to make it easier for the algorithm to detect larger faces. In this case, we have specified a scale factor of 1.1, indicating that we want to reduce the image size by 10%.

4. minNeighbors:
The third parameter in this method is called minNeighbors. The cascade classifier applies a sliding window through the image to detect faces in it. You can think of these windows as rectangles.
Initially, the classifier will capture a large number of false positives. These are eliminated using the minNeighbors parameter, which specifies the number of neighboring rectangles that need to be identified for an object to be considered a valid detection.
To summarize, passing a small value like 0 or 1 to this parameter would result in a high number of false positives, whereas a large number could lead to losing out on many true positives.
The trick here is to find a tradeoff that allows us to eliminate false positives while also accurately identifying true positives.

#Step 6: Drawing a Bounding Box

Now that the model has detected the faces within the image, let’s run the following lines of code to create a bounding box around these faces:
"""

for (x, y, a, b) in faces:
    img = cv2.rectangle(img, (x, y), (x+a, y+b), (255, 0, 0), 4)

"""The faces variable is an array with four values: the x and y axis in which the faces were detected, and their width and height. The above code iterates over the identified faces and creates a bounding box that spans across these measurements.

The parameter 255,0,0 represents the color of the bounding box, which is red, and 4 indicates its thickness.

#Step 7: Displaying the Image

Now, let’s use the Matplotlib library to display the image:
"""

plt.imshow(img)
plt.axis('off')

"""Great!

The model has successfully detected the human faces in this image and created a bounding box around it.
"""