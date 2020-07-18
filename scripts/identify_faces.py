import cv2
import numpy as np
import os
from PIL import Image

source = cv2.VideoCapture('data/blurred_differential_videos/blurred_differential.mp4')

font = cv2.FONT_HERSHEY_SIMPLEX

upper_body_clsfr = cv2.CascadeClassifier('Lib/site-packages/cv2/data/haarcascade_upperbody.xml')

while (True):

    ret, img = source.read()
    current_frame_pixels = np.asarray(img)

    key = cv2.waitKey(1)
    if (key == 27) or not current_frame_pixels.any():
        break

    bodies = upper_body_clsfr.detectMultiScale(
        img,
        scaleFactor=1.2,
        minSize = (30,40)
    )

    for x, y, w, h in bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    caption_string = 'Dimensions: ' + str(current_frame_pixels.shape)
    cv2.putText(img, caption_string, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)

    cv2.imshow('LIVE', img)

cv2.destroyAllWindows()
source.release()

