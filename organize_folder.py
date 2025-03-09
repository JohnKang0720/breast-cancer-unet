import shutil
import os

# Move files into corresponding folders

image_folder = os.listdir('./malignant')

os.makedirs('./mask', exist_ok=True)
os.makedirs('./no_mask', exist_ok=True)


for image in image_folder:
    if 'mask' in image:
        shutil.move(f'./malignant/{image}', './mask')
    else:
        shutil.move(f'./malignant/{image}', './no_mask')

os.rmdir('./malignant')

