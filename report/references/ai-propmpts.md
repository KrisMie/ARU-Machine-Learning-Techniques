# AI Promopts

This document contains AI prompts used during the work oin this project

### AI Prompt Disclosure

AI Tool: OpenAI ChatGPT
Purpose: Research assistance, theoretical explanations,
implementation guidance, debugging and interpretation.

## Project Preparation

1. "I am starting my ARU MSc Machine Learning Techniques coursework, using the PlantVillage colour image dataset.
I want you to act as a tutor and research assistant, guiding me through the assignment rather than generating a complete solution.
I have already created a Git repository with directories for assignment instructions, data, source notebooks, model outputs and reports.
We will begin with the dataset and exploratory data analysis, but first I want to understand the dataset structure, the importance of leaf-grouped splitting and how to design a reproducible ML experiment.
Please guide me one step at a time. Explain the theory and mathematics when appropriate, recommend authoritative academic and technical references, and allow me to write and understand my own Python code.
Clearly distinguish assignment requirements from optional improvements. Keep track of where we are in the coursework when we explore related topics.
I also need to record my AI prompts for academic disclosure, so remind me to preserve substantive questions used in preparing the coursework.
Some of the other reference material i have on hand are:
Python Machine Learning — Sebastian Raschka
Artificial Intelligence: A Modern Approach — Stuart Russell and Peter Norvig
An Introduction to Statistical Learning: With Applications in Python
https://github.com/spMohanty/PlantVillage-Dataset
https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2016.01419/full
but feel free to suggest other reference material either in text/digital book format or other online resources like official documentations (i.e. scikit, tensorflow, pandas, python) or educational videos."

## Dataset Exploration

2. I have not download the dataset yet. The assessment task description says:
"Link to the dataset: PlantVillage Dataset — https://github.com/spMohanty/PlantVillage-Dataset
The repository provides colour, grayscale and segmented image versions. Use the colour images in raw/color for this assignment. Each class folder represents a crop and disease combination, or a healthy crop class; use these folder names as the target labels. Explore and report the class names and image counts in your downloaded data." 
and 
"2.	Download the PlantVillage dataset from the provided link and use the raw/color images. Create reproducible training, validation and test splits, keeping images of the same leaf together using the repository’s leaf-grouping metadata. Apply augmentation only to the training data."

The repo documentation says I can either use it via the huggingface:
 pip install datasets
then use it to load_dataset()
OR
clone repo

Which approach is more appropriate for task wording? It sounds like I should download the images from teh repo and create my splits instead of hugging face ready made splits?

3. Are we allowed to use these additional (metadata) files. Can you check assignment wording?
It says "The repository provides colour, grayscale and segmented image versions. Use the colour images in raw/color for this assignment. Each class folder represents a crop and disease combination, or a healthy crop class; use these folder names as the target labels. Explore and report the class names and image counts in your downloaded data." + "2.	Download the PlantVillage dataset from the provided link and use the raw/color images. Create reproducible training, validation and test splits, keeping images of the same leaf together using the repository’s leaf-grouping metadata. Apply augmentation only to the training data." Will using these files go against the assignment?

4. Used AI assistance to examine and interpret the 'leaf.json' metadata file.

5. My total count is 54305, while the repository says there are 54306 images - is my code missing one image?

When you introduce new concepts, like image/data balancing, augmentation, oversampling or other, point me to the reading sections, chapters about it in our reference materials if possible so i can learn more.

6. To display one random image I have:
my_random = 2441156
random.seed(my_random)

img = Image.open(random.choice(all_images))

print(f'Image size: {img.size}')
print(f'Image mode: {img.mode}')
print(f'Image format: {img.format}')

display(img)

but it displays different image everytime - should it not be the same since i provided seed?

7. That image is not an image of a leaf at all - we should remove it? Should i do it manually (i know the path) or programatically?

8. It belongs to healthy "Pepper,_bell___healthy" class/directory.
Question: should i remove it from all_images after the code that found it, or modify the original path? If i modify original, the notebook won't show the full story. I do this in eds.ipynb - will i be able to export the prepared dataset to use in other notebooks files where I will build the models?