import cv2
import numpy as np
import glob

frameSize = (800, 800)

out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, frameSize)

for filename in glob.glob('Frames/*.png'):
    img = cv2.imread(filename)
    out.write(img)

out.release()