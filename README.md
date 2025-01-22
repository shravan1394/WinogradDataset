# Winograd Dataset 
The dataset used for the paper, "[The Curious Mind: Eye Movements to Maximize Scene Understanding.](https://osf.io/preprints/psyarxiv/6c8gf?raw=true)” 

## Motivation
This study aims to understand how humans explore scenes while freely viewing scenes. To this end, we provide experimental evidence for a new theory. During free viewing (no instructions), humans aim to extract visual information to understand a scene, and their eye movements have a functional importance and are directed to objects that provide an accurate understanding of the scene. We show empirical evidence that humans direct their eyes most frequently to objects that are critical to the understanding of the scene, even if these are not the most salient, nor judged to be the most meaningful object (meaning maps), nor gazed at or to be grasped by an agent in the scene.  The theory might seem intuitive, but providing a strong scientific theory and empirical evidence has been difficult due to many obstacles: lack of methods to objectively and quantitatively measure the contribution of an object or scene region to scene understanding, no methods to create images that dissociate saliency, local meaningfulness judgments (meaning maps) from relevance to scene understanding, no experimental designs to demonstrate that eye movements during free viewing have functional value to accurately understanding scenes.

## Contents:

### Winograd Images: 
18 pairs in total (Set1: contains one image of each pair, Set2: contains the other image of each pair)
Each image pair visually looks very similar, but when asked to describe it, people describe it entirely differently. This allows us to study scene understanding while preserving the low-level visual aspects. The figure below shows an example of such a stimuli pair along with the prediction heatmaps of a leading low-level saliency model ([GBVS](http://papers.neurips.cc/paper/3095-graph-based-visual-saliency.pdf?raw=true)). The descriptions given by people to the pair are completely different, while the low-level saliency predictions are similar.

![Alt text](/ReadMeFiles/WinogradExample.png?raw=true "Optional Title")

### Erased Object images
350 images in total (contains the Winograd images and all its digitally manipulated versions with one object removed in each image)

This work also introduces a new quantitative approach to measure the contribution of an object to scene understanding by assessing the impact of deleting each object from the image on the scene description relative to the gold standard description. We show an example of our procedure to determine the object most critical to understanding the scene.

![Alt text](/ReadMeFiles/ObjectErasure Procedure.png?raw=true "Optional Title")
![Alt text](/ReadMeFiles/ObjectErasureProcedure.png?raw=true "Optional Title")
