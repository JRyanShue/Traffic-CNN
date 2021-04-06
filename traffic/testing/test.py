import cv2
import numpy as np
import os
import sys
import tensorflow as tf
import traffic

"""
Script for testing certain libraries
"""

# test_img = cv2.imread('gtsrb/0/00000_00000.ppm')
# output = cv2.resize(test_img, (traffic.IMG_WIDTH, traffic.IMG_HEIGHT))
# print(type(test_img))
# print(test_img)

# dirPath = os.path.join('C:', os.sep, 'Users', 'jryan')

images = []
labels = []

for category in range(traffic.NUM_CATEGORIES):
    # folder_path = os.path.join('traffic', os.sep, 'gtsrb', str(category))  # folder directory
    folder_path = os.path.join('../gtsrb', str(category))
    print(folder_path)
    for file in os.listdir(folder_path):
        print("file name:", file)
        add_image = cv2.imread(os.path.join(folder_path, file))  # read image
        add_image = cv2.resize(add_image, (traffic.IMG_WIDTH, traffic.IMG_HEIGHT))  # standard resize
        images.append(add_image)  # add image
        labels.append(category)  # add label for image

        # print("shape of image array:", add_image.shape)

        # print("added:", add_image, "for category:", category)

# print(dirPath)


