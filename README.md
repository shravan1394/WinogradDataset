# Winograd Images: Eyemovement Dataset 
The eye movement dataset is collected as part of the paper, "[The Curious Mind: Eye Movements to Maximize Scene Understanding.](https://osf.io/preprints/psyarxiv/6c8gf?raw=true)” 

This study aims to understand how humans explore scenes while freely viewing scenes. We hypothesize that people try to understand scenes when they freely view them by default. To this end, We have developed a dataset of image pairs that dissociates low-level saliency ([GBVS](http://papers.neurips.cc/paper/3095-graph-based-visual-saliency.pdf?raw=true)) and locally meaningful regions ([Meaning Maps](https://jov.arvojournals.org/article.aspx?articleid=2685927?raw=true)) from regions important to understand a scene. We call them the Winograd Image pairs, inspired by the [Winograd Schema Challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html) for sentences (Levesque, H et. al, 2012). Each image pair visually looks very similar, but when asked to describe it, people describe it entirely differently. This allows us to study scene understanding while preserving the low-level visual aspects.

The Winograd Images and the corresponding measured/predicted fixation heatmaps can be found here (HYPERLINK will be added)

## Accessing Eye movement Data

### Dependencies
Please install the following
1. Python 3.6 or above
2. numpy
3. cv2
4. json_lines

The ExampleCodeUsage.py file provides a sample code to access and plot eye movement data and generate fixation heatmaps. The Figure below shows an example image pair with the heat maps generated using the code.

![Alt text](/ReadMeFiles/ExampleImagePair.png?raw=true "Optional Title")


## Contents:

### Winograd Images: 
18 pairs in total (Set1: contains one image of each pair, Set2: contains the other image of each pair)
Each image pair visually looks very similar, but when asked to describe it, people describe it entirely differently. This allows us to study scene understanding while preserving the low-level visual aspects. The figure below shows an example of such a stimuli pair along with the prediction heatmaps of a leading low-level saliency model ([GBVS](http://papers.neurips.cc/paper/3095-graph-based-visual-saliency.pdf?raw=true)). The descriptions given by people to the pair are completely different, while the low-level saliency predictions are similar.

![Alt text](/ReadMeFiles/WinogradExample.png?raw=true "Optional Title")

### Erased Object images
350 images in total (contains the Winograd images and all its digitally manipulated versions with one object removed in each image). All images ending with an "_0" corresponds to the original unaltered image while the rest corresponds to the manipulated versions

This work also introduces a new quantitative approach to measure the contribution of an object to scene understanding by assessing the impact of deleting each object from the image on the scene description relative to the gold standard description. We show an example of our procedure to determine the object most critical to understanding the scene.

![Alt text](/ReadMeFiles/ObjectErasureProcedure.png?raw=true "Optional Title")

### Subject Data
Contains all deidentified subject information including their eye movement data collected for this study
### JSON files (all under JSONS folder)
1. WinogradImagesJson.jsonl: contains basic information about all Winograd Image Pairs (usage could be found in the example code)
2. ErasedObjects_Data.jsonl: contains descriptions for each object removed and gold standard descriptions (descriptions for the original unaltered images).
3. ForcedFixationData.jsonl: contains descriptions collected while people are forced to fixate(500 ms) at locations that are critical and not critical to scene understanding. 


