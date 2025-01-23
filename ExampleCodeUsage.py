from User import User
import constants
import json_lines
import os
import cv2
import numpy as np

Subjects = os.listdir("SubjectData")  # Contains all subject eye movement data

Condition = {0: "Study1",  # Free viewing
             1: "Study2",  # Scene Description
             2: "Study3",  # Object Search
             3: "Study5"}  # Counting Objects
studyname = {"Study1": "Free Viewing",
             "Study2": "Scene Description",
             "Study3": "Object Search",
             "Study5": "Counting Objects"}
Type = {0: 'BL',  # BL: Baseline Image
        1: 'OM'}  # OM: Object locations Manipulated (Winograd Pair)


def psychopy_image(path):  # Maps image to the psychophysics study dimensions
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
    return background


def invert_psychopy_image(image, path):  # converts a given image back to original dimensions
    img = cv2.imread(path)
    aspectRatio = img.shape[1] / img.shape[0]
    dim = (int(aspectRatio * constants.IMG_HEIGHT), constants.IMG_HEIGHT)
    H = constants.IMG_HEIGHT
    W = dim[0]
    start = [constants.Psych2CV[0] - int(H / 2), constants.Psych2CV[1] - int(W / 2)]
    if start[1] < 0:
        start[1] = 0
    image = image[start[0]:start[0] + H, start[1]:start[1] + W, ...]

    return image


imgsPath = []
items = []
with open(os.path.join('JSONS', 'WinogradImagesJson.jsonl'), 'rb') as f:  # opening file in binary(rb) mode
    for item in json_lines.reader(f):
        impath = {'BL': os.path.join('data', 'WinogradImages', item['Baseline']),
                  'OM': os.path.join('data', 'WinogradImages', item['ObjectManipulation'])}
        imgsPath.append(impath)

        items.append(item)


condition = Condition[0]  # Free viewing (change it to other conditions by changing the index number)
for impath in imgsPath:
    img = {'BL': psychopy_image(impath['BL']),
           'OM': psychopy_image(impath['OM'])}
    attentionMap = {'BL': np.zeros(img['BL'].shape[:2]),
                    'OM': np.zeros(img['OM'].shape[:2])}
    i = int(impath['BL'].split('\\')[-1].split("_")[0]) - 1
    for subName in Subjects:
        if os.path.exists("SubjectData/" + subName + "/" + condition + "/"):
            typ = os.listdir("SubjectData/" + subName + "/" + condition + "/")[0]
            if typ not in img:
                continue

            subject = User(subName, condition, typ)  # Subject class that handles the data for each subject
            order = subject.get("TrialOrder")  # Order of trials the participant saw the images
            eyeData = subject.get("EyeTrackData")  # All eye tracking information
            trials = subject.get("TrialsCompleted")  # Number of trials completed
            idx = order.index(i)  # Get the index for the current image
            if condition == Condition[1]:  # Scene description
                descriptions = subject.get("Descriptions")[idx]  # Description given by this subject for this image

            for fixations in eyeData[idx]['AllFixations']:  # Accessing fixations for the given subject and image
                if fixations[0] < attentionMap[typ].shape[1]:
                    attentionMap[typ][int(fixations[1]), int(fixations[0])] += 1


    # Removing background from image
    attentionMap['BL'] = invert_psychopy_image(attentionMap['BL'], impath['BL'])
    attentionMap['OM'] = invert_psychopy_image(attentionMap['OM'], impath['OM'])
    img['BL'] = invert_psychopy_image(img['BL'], impath['BL'])
    img['OM'] = invert_psychopy_image(img['OM'], impath['OM'])

    # Convolving fixations with Gaussian kernel of 0.5 dva standard deviation
    attentionMap['BL'] = cv2.GaussianBlur(attentionMap['BL'], (51, 51), 10)
    attentionMap['OM'] = cv2.GaussianBlur(attentionMap['OM'], (51, 51), 10)

    # Normalizing the attention maps
    attentionMap['BL'] = np.array(attentionMap['BL'] / np.max(attentionMap['BL']) * 255, np.uint8)
    attentionMap['OM'] = np.array(attentionMap['OM'] / np.max(attentionMap['OM']) * 255, np.uint8)

    # Making color maps
    ColorMap = {'BL': cv2.applyColorMap(attentionMap['BL'], cv2.COLORMAP_JET),
                'OM': cv2.applyColorMap(attentionMap['OM'], cv2.COLORMAP_JET)}

    # Blending colormap with the image
    alpha = 0.65
    blend = {'BL': np.array(alpha * ColorMap['BL'] + (1 - alpha) * img['BL'], np.uint8),
             'OM': np.array(alpha * ColorMap['OM'] + (1 - alpha) * img['OM'], np.uint8)}

    # Display Winograd Image Pair
    print("Winograd Image Pair " + str(i + 1))
    cv2.imshow(studyname[condition] + " Fixation Heatmap: Pair 1", blend['BL'])
    cv2.imshow(studyname[condition] + " Fixation Heatmap: Pair 2", blend['OM'])
    cv2.waitKey(0)


