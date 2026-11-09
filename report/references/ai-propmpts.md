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

2. "I have not download the dataset yet. The assessment task description says:
"Link to the dataset: PlantVillage Dataset — https://github.com/spMohanty/PlantVillage-Dataset
The repository provides colour, grayscale and segmented image versions. Use the colour images in raw/color for this assignment. Each class folder represents a crop and disease combination, or a healthy crop class; use these folder names as the target labels. Explore and report the class names and image counts in your downloaded data." 
and 
"2.	Download the PlantVillage dataset from the provided link and use the raw/color images. Create reproducible training, validation and test splits, keeping images of the same leaf together using the repository’s leaf-grouping metadata. Apply augmentation only to the training data."

The repo documentation says I can either use it via the huggingface:
 pip install datasets
then use it to load_dataset()
OR
clone repo

Which approach is more appropriate for task wording? It sounds like I should download the images from teh repo and create my splits instead of hugging face ready made splits?"

3. "Are we allowed to use these additional (metadata) files. Can you check assignment wording?
It says "The repository provides colour, grayscale and segmented image versions. Use the colour images in raw/color for this assignment. Each class folder represents a crop and disease combination, or a healthy crop class; use these folder names as the target labels. Explore and report the class names and image counts in your downloaded data." + "2.	Download the PlantVillage dataset from the provided link and use the raw/color images. Create reproducible training, validation and test splits, keeping images of the same leaf together using the repository’s leaf-grouping metadata. Apply augmentation only to the training data." Will using these files go against the assignment?"

4. Used AI assistance to examine and interpret the 'leaf-map.json' metadata file.

5. "My total count is 54305, while the repository says there are 54306 images - is my code missing one image?

When you introduce new concepts, like image/data balancing, augmentation, oversampling or other, point me to the reading sections, chapters about it in our reference materials if possible so i can learn more."

6. "To display one random image I have:
my_random = 2441156
random.seed(my_random)

img = Image.open(random.choice(all_images))

print(f'Image size: {img.size}')
print(f'Image mode: {img.mode}')
print(f'Image format: {img.format}')

display(img)

but it displays different image everytime - should it not be the same since I provided seed?"

7. "That image is not an image of a leaf at all - we should remove it? Should I do it manually (I know the path) or programatically?"

8. "It belongs to healthy "Pepper,_bell___healthy" class/directory.
Question: should I remove it from all_images after the code that found it, or modify the original path? If i modify original, the notebook won't show the full story. I do this in eds.ipynb - will i be able to export the prepared dataset to use in other notebooks files where I will build the models?"

9. "Keys with exactly one value: 38156
Keys with more than one value: 2172
Maximum number of values for a single key: 3

Question:
That metadata file has 40,328 keys according to my code. The "Using Deep Learning for Image-Based Plant Disease Detection" article says 41,112 -why the discrepancy. Also if the keys are pointing to image files, why in the leaf-map.json there is for example:
" "rs_hl 5922": [
        "Soybean___healthy:::372.0",
        "Apple___healthy:::47.0"
    ],
    "rs_hl 5923": [
        "Soybean___healthy:::372.0",
        "Apple___healthy:::47.0"
    ],
    "rs_hl 5920": [
        "Soybean___healthy:::372.0",
        "Apple___healthy:::47.0"
    ],
    "rs_hl 5921": [
        "Soybean___healthy:::372.0",
        "Apple___healthy:::47.0"
    ]," - how can one file id represent two different plant species?"

10. "Total_individual_mappings = sum(len(values) for values in images_metadata.values())
print(f'Total number of individual mappings: {total_individual_mappings}')

Total number of individual mappings: 42520"

11. "I changed the variable name from metadata_id to image_id as I feel it comes from image name and implemented mapping retreival from images_metadata:

random.seed(my_random)

images_to_check = random.sample(clean_images, 3)

print(f'Number of images to check: {len(images_to_check)}\n')

for img_path in images_to_check:
    image_id = get_image_id(img_path)

    mapping = images_metadata.get(image_id)

    print(f'Class directory: {img_path.parent.name}')
    print(f'Filename: {img_path.name}')
    print(f'Image ID: {image_id}')
    print(f'Mapping: {mapping}\n')

Output:

Number of images to check: 3

Class directory: Soybean___healthy
Filename: 637c4131-9177-4e3c-88fa-7fcacbca33ba___RS_HL 4655.JPG
Image ID: rs_hl 4655
Mapping: ['Soybean___healthy:::218.0']

Class directory: Tomato___Leaf_Mold
Filename: 790cfb1d-4926-46bb-bd50-b750e823c72a___Crnl_L.Mold 7130.JPG
Image ID: crnl_l.mold 7130
Mapping: ['Tomato___Leaf_Mold:::121.0']

Class directory: Tomato___Bacterial_spot
Filename: 61a05330-1086-4891-8482-3f422ff59492___GCREC_Bact.Sp 3429.JPG
Image ID: gcrec_bact.sp 3429
Mapping: ['Tomato___Bacterial_spot:::121.0']

What should be the next step?
Do I have to manually make the datasets and based on leaf-map.json and images and select the images interpreting the assignment wording: "2.	Download the PlantVillage dataset from the provided link and use the raw/color images. Create reproducible training, validation and test splits, keeping images of the same leaf together using the repository’s leaf-grouping metadata. Apply augmentation only to the training data." and "3.	Data Processing/Feature Engineering: Describe the image preprocessing and feature engineering methods that you have used. Explain how these methods work mathematically for your dataset and document your training, validation and test splits and how you avoided data leakage." - the repository also contains  what seem to be already sorted leafmaps?"

12. "It looks like "Apple_Frogeye Spot" has entries in leaf_maps csv and leaf-map.json following "jr_frge.s" pattern but the image directory name is "Apple___Black_rot" so the images won't be selected if compared to class name taken from directory. there may be more instances like that."

13. "I renamed "selected_group" to "leaf_id" since this var only holds the leaf id that applies to multiple leaves.
Will my key[value] get replaced in mappings dictionary when it will encounter class with different leaf_id and I will lend up having only one id per class?
Check my code:

random.seed(my_random)

images_to_check = random.sample(clean_images, 3)

print(f'Number of images to check: {len(images_to_check)}\n')

for img_path in images_to_check:
    image_id = get_image_id(img_path)

    print(f'Filename: {img_path.name}')
    print(f'Image ID: {image_id}')
    
    mappings = {}

    mapping = images_metadata.get(image_id)

    print(f'Mapping: {mapping}')

    for item in mapping:
        split = split_metadata(item)
        mappings[split[0]] = split[1]
        print(f'Split mapping:\n    Leaf class: {split[0]}\n    Leaf group: {split[1]}')

    class_name = img_path.parent.name
    leaf_id = mappings.get(class_name)

    print(f'Class: {class_name}')
    print(f'Leaf ID: {leaf_id}\n')"

14. "How to test test the missing-metadata case and whet do you mean by "One final observation: your function currently builds the entire mappings dictionary even though you only need one class-specific value."

15. "Answer: I think normally I'd prefer directory rename - additional metadata lookup alias may introduce more unnecessary complexity and slow down the image retrieval. But to comply with the assignment requirement I need to introduce an mapping alias to keep it reproducible with the repository."

16. "OK this is my implementation of updated get_leaf_id:
def get_leaf_id(image_path: Path, images_metadata: dict, metadata_class_aliases: dict):

    image_id = get_image_id(image_path)
    class_name = image_path.parent.name

    # retrieve corresponding metadata class - this was introduced
    # after the discovery of the need to translate some classes
    # using aliases due to inconsistency between folder and metadata
    # class namings
    
    metadata_class_name = metadata_class_aliases.get(class_name, class_name)

    mapping = images_metadata.get(image_id, [])

    for item in mapping:
      leaf_class, leaf_id = split_metadata(item)

      if leaf_class == metadata_class_name:
          return leaf_id
    
    return None

Now the totals calculated are:

Matched leaf IDs: 41111
Unresolved leaf IDs: 13193
Metadata coverage: 75.70528874484384 %

The test code returns:

apple_leaf_id: 56.0
soybean_image path: C:\Users\kmiel\Repository\ARU MSc\Datasets\PlantVillage-Dataset\raw\color\Soybean___healthy\0007ca44-b81d-475c-b8b5-c226a041f020___RS_HL 6331.JPG
soybean_leaf_id: 405.0

which seems to be correct.

The original paper mentions 42.112 images but I excluded one PNG and the paper does not mention this so mis this the discrepancy?"

17. "The assignment does not seem to be explicitly saying I have to use all 38 classes - only to use folder names as classes. Should I clarify this with my tutor? Does the original paper or other projects train on these images? If I train on these images I risk data leak as I do know which images are of the same leaves? 
I cannot find anything in the repo showing the images assignment to splits."

18. "I think this wording: "2.	Download the PlantVillage dataset from the provided link and use the raw/color images. Create reproducible training, validation and test splits, keeping images of the same leaf together using the repository’s leaf-grouping metadata. Apply augmentation only to the training data." suggests I cannot use the official split (especially having some discrepancies I found) because it splits into training and test, and the assignment expects train, validation and test splits. Do I get that right?"

19. "The HuggingFace repository says "The dataset comes with pre-defined 80/20 train/test splits that preserve the leaf grouping logic (ensuring images of the same leaf do not appear in both sets).  " - does it mean they did not include the images without metadata mapping?"

21. "I have emailed my tutor to clarify the requirements. In the meantime let's investigate whether the 13,193 unresolved images exhibit filename patterns that might provide additional, defensible grouping information—without assuming those patterns establish physical-leaf identity. In case I have to use them."

22. "OK, Does it mean I can use:
"pip install datasets" 
and
"from datasets import load_dataset

Load the dataset (default: color images)
dataset = load_dataset("mohanty/PlantVillage", "color")"

since this is the instruction in repository, and then for example split training set to training + validation?
Or should i inspect color_train.txt and color_test.txt manifests and apply to my images I have on disk?"

23. "I have converted the paths to :
"Sample converted local paths:
raw/color/Strawberry___healthy/80372fb3-2a02-4989-9396-6732cd47cb75___RS_HL 1623.JPG
raw/color/Cherry_(including_sour)___Powdery_mildew/2c972b35-2f4c-4658-ac84-3bb1af7a746d___FREC_Pwd.M 4660.JPG
raw/color/Cherry_(including_sour)___Powdery_mildew/4d53f660-e6ef-47b0-8f12-24a6f7e5ddbb___FREC_Pwd.M 0523.JPG"
but not stored anywhere yet.
Do i have to use the original set or cleaned if i use the repo splits?"