import os
from os.path import join
import shutil
import pandas as pd
from imutils import paths
import argparse
import random

df = pd.read_csv("output.csv")
#print(df)
df['Max'] = df[['back','bleft', 'bright', 'fleft', 'fright', 'front', 'left', 'right']].idxmax(axis=1)
df['Max'] = df['Max']
#print(df)
df1 = df[['image','Max']]
df1 = df1.set_index('image')
#print(df1.loc['9.jpg'])

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--test-images", required=True,
	help="path to the directory of unlabelled images")
args = vars(ap.parse_args())


imagePaths = sorted(list(paths.list_images(args["test_images"])))
random.seed(42)
random.shuffle(imagePaths)
for imagePath in imagePaths:
    col0 = imagePath[imagePath.rfind("/") + 1:]
    #print(col0)
    #print(df1.loc[col0].values[0])
    d = df1.loc[col0].values[0]
    print(d)
    dest_path_back = '/sorted_images/back'
    dest_path_bleft = '/sorted_images/bleft'
    dest_path_bright = '/sorted_images/bright'
    dest_path_fleft = '/sorted_images/fleft'
    dest_path_fright = '/sorted_images/fright'
    dest_path_front = '/sorted_images/front'
    dest_path_left = '/sorted_images/left'
    dest_path_right = '/sorted_images/right'
    print(imagePath)
    if d == 'right':
        print('Moving right images')
        shutil.move(imagePath,dest_path_right)
    if d == 'left':
        print('Moving left images')
        shutil.move(imagePath,dest_path_left)
    if d == 'front':
        print('Moving front images')
        shutil.move(imagePath,dest_path_front)
    if d == 'back':
        print('Moving back images')
        shutil.move(imagePath,dest_path_back)
    if d == 'bleft':
        print('Moving bleft images')
        shutil.move(imagePath,dest_path_bleft)
    if d == 'bright':
        print('Moving bright images')
        shutil.move(imagePath,dest_path_bright)
    if d == 'fright':
        print('Moving fright images')
        shutil.move(imagePath,dest_path_fright)
    if d == 'fleft':
        print('Moving fleft images')
        shutil.move(imagePath,dest_path_fleft)
