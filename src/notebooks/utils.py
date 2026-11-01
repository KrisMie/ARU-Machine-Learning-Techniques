from pathlib import Path
from tqdm import tqdm
from PIL import Image

images_path = Path(__file__).resolve().parent.parent.parent.parent.parent / "Datasets" / "PlantVillage-Dataset" / "raw" / "color"

# the following excluded images were found during the dataset 
# inspectionto be non relevant to the rest of the dataset
excluded_images = {
    Path(__file__).resolve().parent.parent.parent.parent.parent / "Datasets" / "PlantVillage-Dataset" / "raw" / "color" /"Pepper,_bell___healthy/42f083e2-272d-4f83-ad9a-573ee90e50ec___Screen Shot 2015-05-06 at 4.01.13 PM.png"
}

def load_images():
    """
    Scans the PlantVillage dataset directory, filters valid extensions,
    excludes specified bad images, and validates modes/formats.
    Returns data as dictionary that may be required by other notebooks.
    """

    # 1. Get classes (directories)
    classes = sorted([x.name for x in images_path.iterdir() if x.is_dir()])
    number_classes = len(classes)

    valid_extensions = {'.jpg', '.jpeg', '.png'}
    class_counts = []
    class_distribution = {}
    all_images = []

    # 2. Collect images per class (directory)
    for x in classes:
        class_dir = images_path / x

        class_images = [i for i in class_dir.iterdir() if i.is_file() and i.suffix.lower() in valid_extensions]

        class_counts.append(len(class_images))
        class_distribution[x] = len(class_images)
        all_images.extend(class_images)

    class_counts.sort()
    class_distribution = dict(sorted(class_distribution.items(), key=lambda item: item[1]))

    # 3. Filter out excluded images
    clean_images = [
        image for image in all_images
        if image not in excluded_images
    ]

    # 4. Validate format and mode properties
    all_rgb = True
    print("Validating image properties (RGB / JPEG)...")
    for image in tqdm(clean_images):
        with Image.open(img_path := image) as img:
            if img.mode != "RGB" or img.format != "JPEG":
                all_rgb = False

    # Return a everything other notebooks may need (dictionary)
    return {
        "images_path": images_path,
        "classes": classes,
        "number_classes": number_classes,
        "class_counts": class_counts,
        "class_distribution": class_distribution,
        "clean_images": clean_images,
        "all_rgb": all_rgb
    }