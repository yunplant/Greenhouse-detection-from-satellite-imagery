import os
import glob
import numpy as np
import math
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def vertical_slice(out_name, outdir, slice_size):
        img = Image.open('C:/Users/ys/Desktop/data_process/33.2998_126.2188.png')
        width, height = img.size
        upper = 0
        left = 0
        slices = int(math.ceil(height / slice_size))
        count = 1
        for slice in range(slices):
            if count == slices:
                lower = height
            else:
                lower = int(count * slice_size)

            bbox = (left, upper, width, lower)
            working_slice = img.crop(bbox)
            upper += slice_size
            working_slice.save(os.path.join(outdir, "slice_" + str(np.random.randint(99999999)) + out_name + "_" + str(
                count) + ".png"))
            count += 1


def horizontal_slice(out_name, outdir, slice_size):
    for f in glob.glob(r'C:\Users\ys\Desktop\data_process\ver1\*.png'):
        img = Image.open(f)
        width, height = img.size
        upper = 0
        left = 0
        slices = int(math.ceil(width / slice_size))
        count = 1
        for slice in range(slices):
            if count == slices:
                right = width
            else:
                right = int(count * slice_size)
            bbox = (left, upper, right, height)
            working_slice = img.crop(bbox)
            left += slice_size
            working_slice.save(os.path.join(outdir, "slice_image_" + '_' + str(
                np.random.randint(99999999)) + out_name + "_" + str(count) + ".png"))
            count += 1

vertical_slice('1','C:/Users/ys/Desktop/data_process/ver1',1000)
horizontal_slice('res','C:/Users/ys/Desktop/data_process/hor1',1000)