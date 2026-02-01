# Winograd Images: Eyemovement Dataset 
This repository provides access to the eye movement data collected as part of the paper, "[Eye movements during free viewing to maximize scene understanding](https://www.nature.com/articles/s41467-025-67673-w)” (Published in Nature Communications). 

This study aims to understand how humans explore scenes while freely viewing them. We hypothesize that people try to understand scenes when they freely view them by default. To this end, We have developed a dataset of image pairs that dissociates low-level saliency ([GBVS](http://papers.neurips.cc/paper/3095-graph-based-visual-saliency.pdf?raw=true)) and locally meaningful regions ([Meaning Maps](https://jov.arvojournals.org/article.aspx?articleid=2685927?raw=true)) from regions important to understand a scene. We call them the Winograd Image pairs, inspired by the [Winograd Schema Challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html) for sentences (Levesque, H et. al, 2012). Each image pair visually looks very similar, but when asked to describe it, people describe it entirely differently. This allows us to study scene understanding while preserving the low-level visual aspects. We collect eye movements to the Winograd Image pairs for the four tasks (details given below).

The Winograd Image pairs and the corresponding measured/predicted fixation heatmaps can be found here ([link](https://data.mendeley.com/datasets/z6jb259pcd/1))

Please cite "[The Curious Mind: Eye Movements to Maximize Scene Understanding.](https://osf.io/preprints/psyarxiv/6c8gf?raw=true)” when using this dataset

## Dependencies
Please install the following
1. Python 3.6 or above
2. numpy
3. cv2
4. json_lines

Installation time: less than 5 mins

## Accessing Eye movement Data
Eye movements were collected for four different conditions as part of the study. Each condition was associated with a specific task (Free viewing, Scene description, Object search, and Counting objects). We provide access to all the eye movement data collected in this study. 


The ExampleCodeUsage.py file provides a sample code to access and plot eye movement data and generate fixation heatmaps. The Figure below shows an example image pair with the heat maps generated using the code.

![Alt text](/ReadMeFiles/ExampleImagePair.png?raw=true "Optional Title")


## Generating Scene Understanding Maps for the images used in our study
The GenerateSUMap.py file provides a sample code to generate SU maps for the images used in the study. The Figure below shows an example image generated using the code. The code takes about 10 mins to compute the scene understanding map for 36 images in our dataset.

![Alt text](/ReadMeFiles/SUMapExample.png?raw=true "Optional Title")


## Visualize bounding boxes used for different object categories
The ObjectCategoriesExample.py file provides code to access the bounding boxes to various object categories defined in the study. The object categories defined in the study are
1. Person
2. Search Target Object
3. SURelevant
4. SURelevant with predicitons to people included
5. SUIrrelevant
6. DeepGaze
7. Meaning Maps
8. GBVS
9. Perceived Grasped/Looked At

The figure below shows an example of the program's output. The code allows you to choose the category you want to visualize. The example below visualizes the bounding box over people in scenes.
![Alt text](/ReadMeFiles/ExampleBoundingBox.png?raw=true "Optional Title")

## Contents:

### Winograd Image Pairs: 
18 pairs in total (Set1: contains one image of each pair, Set2: contains the other image of each pair)
The low-level visual features of each image pair are very similar. At the same time, the information required to understand the scene for each image pair requires looking at different regions of the scene.  The figure below shows an example of such a stimuli pair along with the prediction heatmaps of a leading low-level saliency model ([GBVS](http://papers.neurips.cc/paper/3095-graph-based-visual-saliency.pdf?raw=true)). The descriptions given by people to the pair are entirely different, while the low-level saliency predictions are similar.

![Alt text](/ReadMeFiles/WinogradExample.png?raw=true "Optional Title")

### Erased Object images
366 images in total (contains the Winograd images and all its digitally manipulated versions with one object removed in each image). All images ending with an "_0" correspond to the original unaltered image, while the rest correspond to the manipulated versions.

This work also introduces a new quantitative approach to measuring an object's contribution to scene understanding by assessing the impact of deleting each object from the image on the scene description relative to the gold standard description (details about how to access these descriptions are given below). We show an example of our procedure to determine the object most critical to understanding the scene.

![Alt text](/ReadMeFiles/ObjectErasureProcedure.png?raw=true "Optional Title")

### Subject Data
Contains all deidentified subject information, including their eye movement data collected for this study

### JSON files (all under JSONS folder)
1. WinogradImagesJson.jsonl: contains basic information about all Winograd Image Pairs (usage could be found in the example code)
2. ObjectsErasedData.jsonl: contains descriptions for each object removed and gold standard descriptions (descriptions for the original unaltered images).
3. ForcedFixationData.jsonl: contains descriptions collected while people are forced to fixate(500 ms) at locations that are critical and not critical to scene understanding. 


