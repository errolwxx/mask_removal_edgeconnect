import os
import numpy as np
import random

images_path = "./datasets/pins_celebs/images"
masks_path = "./datasets/pins_celebs/masks"

allimages = [os.path.join(images_path, f) for _, _, files in os.walk(images_path) for f in files]
allmasks = [os.path.join(masks_path, f) for _, _, files in os.walk(masks_path) for f in files]