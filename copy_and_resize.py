import os
from PIL import Image


from torchvision.transforms import transforms
import torchvision.transforms.functional as fn

ORIGINAL_IMG_DIR = r'/home/alex/git/pytorch-CycleGAN-and-pix2pix/datasets/giger_original/originals'
COPY_IMG_DIR = r'/home/alex/git/pytorch-CycleGAN-and-pix2pix/datasets/giger_original/modified'

img_paths = []
for img_name in os.listdir(ORIGINAL_IMG_DIR):
    img_paths.append(os.path.join(ORIGINAL_IMG_DIR, img_name))

for img_path in img_paths:
    print(img_path)
    img_name = img_path.split("/")[-1]
    with Image.open(img_path) as img_file:
        copy_path = os.path.join(COPY_IMG_DIR, img_name)
    #     resized = fn.resize(img_file, [256,256])
        img_file.save(copy_path)
