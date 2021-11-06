import cv2
import numpy as np
import glob
import os
from os.path import isfile, join
import re

def Images2Video (pathIn, pathOut, frameSize):
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files.sort(key=lambda f: int(re.sub('\D', '', f)))

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), 20, frameSize)

    for filename in files:
        img = cv2.imread(pathIn + filename)
        out.write(img)

    out.release()
