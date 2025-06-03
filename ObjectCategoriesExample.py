import cv2
import json_lines
import os
import numpy as np

## Required Constants
BACKGROUND_SIZE = (1024, 1280, 3)
IMG_HEIGHT = 577  # approx 13 dva
MONITOR_RESOLUTION = (1280, 1024)
IMAGE_Y_DISPLACEMENT = 100  # Psychopy coordinates
IMAGE_X_DISPLACEMENT = 0  # Psychopy coordinates
Psych2CV = [int(MONITOR_RESOLUTION[1] / 2) - IMAGE_Y_DISPLACEMENT,
            int(MONITOR_RESOLUTION[0] / 2) + IMAGE_X_DISPLACEMENT]


def psychopy_image(path):  # Converts image to psychopy coordinates
    background = np.ones(BACKGROUND_SIZE, np.uint8) * 128
    img = cv2.imread(path)
    aspectRatio = img.shape[1] / img.shape[0]
    dim = (int(aspectRatio * IMG_HEIGHT), IMG_HEIGHT)
    H = IMG_HEIGHT
    W = dim[0]
    start = [Psych2CV[0] - int(H / 2), Psych2CV[1] - int(W / 2)]
    if start[1] < 0:
        start[1] = 0
    resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    if resized_img.shape[1] > 1280:
        resized_img = resized_img[:, :1280, :]

    background[start[0]:start[0] + H, start[1]:start[1] + W, :] = resized_img
    return background


def get_image_dim(path):  # get image dimensions
    img = cv2.imread(path)
    aspectRatio = img.shape[1] / img.shape[0]
    dim = (int(aspectRatio * IMG_HEIGHT), IMG_HEIGHT)
    H = IMG_HEIGHT
    W = dim[0]
    start = [Psych2CV[0] - int(H / 2), Psych2CV[1] - int(W / 2)]
    return start, H, W


possibleClasses = ["Person", "TargetObject", "DeepGaze", "GBVS", "MeaningMaps", "SURelevant", "SURelevantwithPeople",
                   "SUIrrelevant", "Perceived Grasped/Looked At"]
cls = possibleClasses[0]  # Put the class name from above for which you want to see the bounding box

with open(os.path.join('JSONS', 'WinogradImagesJson.jsonl'),
          'rb') as f:  # opening file in binary(rb) mode
    for item in json_lines.reader(f):
        img = {
            'ObjectManipulation': psychopy_image(os.path.join("data", "WinogradImages", item['ObjectManipulation'])),
            'Baseline': psychopy_image(os.path.join("data", "WinogradImages", item['Baseline']))}

        for typ in ['Baseline', 'ObjectManipulation']:
            X = item["Results"][typ]["ObjectCategories"]
            for x in X:
                if cls in X[x]:
                    b = [int(a) for a in x.split(" ")]
                    img[typ] = cv2.rectangle(img[typ], b[:2], (b[0] + b[2], b[1] + b[3]),
                                             255, thickness=3)

            start, H, W = get_image_dim(os.path.join("data", "WinogradImages", item[typ]))
            img[typ] = img[typ][start[0]:start[0] + H, start[1]:start[1] + W, :]
            cv2.imshow(typ, img[typ])
        cv2.waitKey(0)
