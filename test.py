# import the necessary packages
from __future__ import print_function
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import random
import pickle
import sys
import csv
import os.path

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to output model file")
ap.add_argument("-t", "--test-images", required=True,
	help="path to the directory of testing images")
ap.add_argument("-b", "--batch-size", type=int, default=32,
	help="size of mini-batches passed to network")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to label binarizer")
args = vars(ap.parse_args())

# grab the image paths and randomly shuffle them
print("[INFO] testing on images...")
imagePaths = sorted(list(paths.list_images(args["test_images"])))
random.seed(42)
random.shuffle(imagePaths)

#file_exists = os.path.isfile(fnames)

f = open('output.csv', 'a')
with f:
	print("CSV file opened")
	fnames = ['image', 'back', 'bleft', 'bright', 'fleft', 'fright', 'front', 'left', 'right']
	writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=fnames)
	writer.writeheader()

# loop over our testing images
	for imagePath in imagePaths:

	# load the image, resize it to a fixed 96 x 96 pixels (ignoring
	# aspect ratio), and then extract features from it
		image = cv2.imread(imagePath)
		image = cv2.resize(image, (96, 96))
		image = image.astype("float") / 255.0
		image = img_to_array(image)
		image = np.expand_dims(image, axis=0)

	# load the network
		print("[INFO] loading network architecture and weights...")
		model = load_model(args["model"])
		mlb = pickle.loads(open(args["labelbin"], "rb").read())

# classify the image using our extracted features and pre-trained
# neural network
		prob = model.predict(image)[0]
		probs = prob*100

	#Getting the values for the labels
		col0 = imagePath[imagePath.rfind("/") + 1:]
		print("col0:"+col0)
		col1 = "{:.2f}".format(probs[0])
		print(col1)
		col2 = "{:.2f}".format(probs[1])
		print(col2)
		col3 = "{:.2f}".format(probs[2])
		print(col3)
		col4 = "{:.2f}".format(probs[3])
		print(col4)
		col5 = "{:.2f}".format(probs[4])
		print(col5)
		col6 = "{:.2f}".format(probs[5])
		print(col6)
		col7 = "{:.2f}".format(probs[6])
		print(col7)
		col8 = "{:.2f}".format(probs[7])
		print(col8)

		print("[DEBUG] just before write rows")
		writer.writerow({'image': col0, 'back': col1, 'bleft': col2, 'bright': col3, 'fleft': col4, 'fright': col5, 'front': col6, 'left': col7, 'right': col8})
		#print(writer)
		print("[DEBUG] after write rows")
	print("Finished printing")
		#sys.stdout.close()
