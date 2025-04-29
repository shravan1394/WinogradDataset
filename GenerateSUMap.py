import json_lines
import jsonlines
import csv
import numpy as np
import constants
import ast
import pandas as pd
import os

import json
import seaborn as sns
import matplotlib.pyplot as plt
import cv2
from natsort import natsorted


def psychopy_image(path):
    background = np.ones(constants.BACKGROUND_SIZE, np.uint8) * 128
    img = cv2.imread(path)
    aspectRatio = img.shape[1] / img.shape[0]
    dim = (int(aspectRatio * constants.IMG_HEIGHT), constants.IMG_HEIGHT)
    H = constants.IMG_HEIGHT
    W = dim[0]
    start = [constants.Psych2CV[0] - int(H / 2), constants.Psych2CV[1] - int(W / 2)]
    if start[1] < 0:
        start[1] = 0
    resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    if resized_img.shape[1] > 1280:
        resized_img = resized_img[:, :1280, :]

    background[start[0]:start[0] + H, start[1]:start[1] + W, :] = resized_img
    return background, start, H, W


allItems = []
items = []
reqdItems = []
ratingList = []
oold = 1
ooold = 1
dat = {}
dataSplitter = []
it = None
maxs = 0
k = 0
l = 0
p = 0
t = 0
q = 0
r = 0
s = 0
avgIrrScores = []
irrScore = 0
allIt = []
X = {}
i = 0
DD = []
k = 0

'''
Each map is subtracted by the lowest score (least impacted)obtained when erasing an object in the corresponding image.
Since the background table or floor would technically also have least impact on the scene description, we would expect 
similar score low scores if we were able to remove them too. So by doing this operation we bring the prediciton of our 
model to the object with least mpact close to that of the background. 
'''
minVal = [4.055555555555555, 3.5555555555555554, 2.7142857142857144, 2.7777777777777777, 2.0555555555555554,
          3.0555555555555554, 1.6111111111111107, 3.2222222222222223, 1.8888888888888893, 2.6428571428571432,
          1.5555555555555554, 4.214285714285714, 2.5, 2.833333333333333, 2.1111111111111107, 2.8, 3.0,
          2.666666666666667, 2.571428571428571, 2.6500000000000004, 3.0555555555555554, 2.95, 2.75, 3.7857142857142856,
          2.2222222222222223, 2.5, 3.3571428571428568, 5.785714285714286, 1.9285714285714288, 2.8571428571428568,
          2.333333333333333, 2.7777777777777777, 4.555555555555555, 3.666666666666667, 2.7142857142857144, 3.0]




Map = [0]
mins = 10000
with open('JSONS/ObjectsErasedData.jsonl', 'rb') as f:  # opening file in binary(rb) mode
    for item in json_lines.reader(f):

        n = int(item['img_fn'].split("_")[1])
        m = int(item['img_fn'].split("_")[-1].split(".")[0])
        o = int(item['img_fn'].split("_")[0])

        if m == 0:

            if np.sum(Map) != 0:
                print("Counter: ", i + 1)
                alpha = 0.8

                Map = Map[start[0]:start[0] + H, start[1]:start[1] + W]
                img1 = img[start[0]:start[0] + H, start[1]:start[1] + W]

                Map = Map / np.max(Map)
                Map = np.array(Map * 255, np.uint8)
                ColorMap = cv2.applyColorMap(Map, cv2.COLORMAP_JET)
                blend = np.array(alpha * ColorMap + (1 - alpha) * img1, np.uint8)
                # minVal.append(mins)  # Uncomment this line when you want to estimate the min values

                '''cv2.imshow("map", blend)
                cv2.waitKey(0)'''

                i += 1

            PP = []
            mins = 10000
            img, start, H, W = psychopy_image(os.path.join("data", "ObjectErased", item["img_fn"]))
            Map = np.zeros(img.shape[:2], np.float64)

        else:
            boxes = item["Boxes"]
            for box in boxes:
                mapx = np.zeros(img.shape[:2], np.float64)
                ''' 
                To avoid the map score for each object erased to be biased by a bad description, we used median rather 
                than mean of the ratings'''

                X = np.median(item["HumanRatings"])

                P = 10 - X - minVal[i]

                ''' P = 10 - X  # use this while estimating the minVal and comment the previous line
                if P < mins:
                    mins = float(P)'''

                # Object centered fixation distribution
                alpha = 0.8
                C = [int(box[1] + box[3] / 2), int(box[0] + box[2] / 2)]
                mapx[C[0], C[1]] += 1
                sigx = 0.29 * box[2]
                sigy = 0.34 * box[3]

                mapx = cv2.GaussianBlur(mapx, (1001, 1001), sigmaX=sigx, sigmaY=sigy)
                mapx = (mapx / np.max(mapx)) * P

                Map += mapx

# The loop comes out before the map generation for the final image. This part of the code generates for the final image.
print("Counter: ", i + 1)
alpha = 0.8

Map = Map[start[0]:start[0] + H, start[1]:start[1] + W]
img1 = img[start[0]:start[0] + H, start[1]:start[1] + W]

Map = Map / np.max(Map)
Map = np.array(Map * 255, np.uint8)
ColorMap = cv2.applyColorMap(Map, cv2.COLORMAP_JET)
blend = np.array(alpha * ColorMap + (1 - alpha) * img1, np.uint8)
# minVal.append(mins)  # Uncomment this line when you want to estimate the min values

'''cv2.imshow("Map", blend)
cv2.waitKey(0)'''
i += 1

print(minVal)
