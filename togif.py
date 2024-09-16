#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import re
import os
from PIL import Image, ImageDraw, ImageFont
from natsort import natsorted

if __name__ == '__main__':

    directory = sys.argv[1]  # get all the arguments

    print(os.listdir(directory))
    all_files = [os.path.join(directory,subdir, file) for subdir in os.listdir(directory) for file in os.listdir(os.path.join(directory,subdir)) if os.path.isfile(os.path.join(directory,subdir, file)) and file.endswith('.png')] 
    all_files = natsorted(all_files)
    print(all_files)
    
    # Create the frames
    frames = []

    for file in all_files:
        new_frame = Image.open(file).convert(mode="P", palette=Image.ADAPTIVE)
        frames.append(new_frame.copy())

    # Save into a GIF file that loops forever
    # Gaussian Potential: duration= 300
    frames[0].save('anim.gif', format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
