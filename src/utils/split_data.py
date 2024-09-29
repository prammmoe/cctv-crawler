import os
import random
import shutil

def create_dir_if_not_exists(directory):
    """
    Helper function to handle directory pathing.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def split_data(SOURCE_DIR, LABEL_DIR, TRAINING_DIR, TRAINING_LABEL_DIR, VALIDATION_DIR, VALIDATION_LABEL_DIR, TESTING_DIR, TESTING_LABEL_DIR):
    """
    ## Params: 
    - SOURCE_DIR: Source images directory
    - LABEL_DIR: Source labels directory
    - TRAINING_DIR: Training images target directory
    - TRAINING_LABEL_DIR: Training labels target directory
    - VALIDATION_DIR: Validation images target directory
    - VALIDATION_LABEL_DIR: Validation labels target directory
    - TESTING_DIR: Testing images target directory
    - TESTING_LABEL_DIR: Testing labels target directory

    ## Example usage
    ```split_data(
            SOURCE_DIR='aic_hcmc2020/images',
            LABEL_DIR='aic_hcmc2020/labels',
            TRAINING_DIR='aic_hcmc2020/train/images',
            TRAINING_LABEL_DIR='aic_hcmc2020/train/labels',
            VALIDATION_DIR='aic_hcmc2020/valid/images',
            VALIDATION_LABEL_DIR='aic_hcmc2020/valid/labels',
            TESTING_DIR='aic_hcmc2020/test/images',
            TESTING_LABEL_DIR='aic_hcmc2020/test/labels'
    )
    """
    images = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    labels = [f for f in os.listdir(LABEL_DIR) if os.path.isfile(os.path.join(LABEL_DIR, f))]

    images.sort()
    labels.sort()

    paired_files = list(zip(images, labels))

    random.seed(42)
    random.shuffle(paired_files)

    train_size = int(len(paired_files) * 0.7)
    val_size = int(len(paired_files) * 0.2)
    # test_size = len(paired_files) - train_size - val_size

    train_files = paired_files[:train_size]
    val_files = paired_files[train_size:train_size + val_size]
    test_files = paired_files[train_size + val_size:]

    # Create directory if directory is not exists
    create_dir_if_not_exists(TRAINING_DIR)
    create_dir_if_not_exists(TRAINING_LABEL_DIR)
    create_dir_if_not_exists(VALIDATION_DIR)
    create_dir_if_not_exists(VALIDATION_LABEL_DIR)
    create_dir_if_not_exists(TESTING_DIR)
    create_dir_if_not_exists(TESTING_LABEL_DIR)

    # Begin loop for splitting
    for image, label in train_files:
        shutil.copyfile(os.path.join(SOURCE_DIR, image), os.path.join(TRAINING_DIR, image))
        shutil.copyfile(os.path.join(LABEL_DIR, label), os.path.join(TRAINING_LABEL_DIR, label))

    for image, label in val_files:
        shutil.copyfile(os.path.join(SOURCE_DIR, image), os.path.join(VALIDATION_DIR, image))
        shutil.copyfile(os.path.join(LABEL_DIR, label), os.path.join(VALIDATION_LABEL_DIR, label))

    for image, label in test_files:
        shutil.copyfile(os.path.join(SOURCE_DIR, image), os.path.join(TESTING_DIR, image))
        shutil.copyfile(os.path.join(LABEL_DIR, label), os.path.join(TESTING_LABEL_DIR, label))

