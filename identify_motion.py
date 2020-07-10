import cv2
import numpy as np
import os
from PIL import Image

try:
    if not os.path.exists('data/differential_frames'):
        os.makedirs('data/differential_frames')
except OSError:
    print('Error: Creating directory of differential video_frames')


source = cv2.VideoCapture('data/bw_videos/blackandwhite_2.mp4')

background_pixels = []
current_frame_pixels = []
pixel_difference = []
first_frame_flag = 0

font = cv2.FONT_HERSHEY_SIMPLEX

differential_frames_path = 'data/differential_frames'
num_leading_zeros = 7
counter = 0

fgbg_extractor = cv2.createBackgroundSubtractorMOG2()

while (True):

    ret, img = source.read()
    current_frame_pixels = np.asarray(img)

    key = cv2.waitKey(1)
    if (key == 27) or not current_frame_pixels.any():
        break

    #if first_frame_flag == 0:
    #    background_pixels = current_frame_pixels
    #    first_frame_flag = 1

    #pixel_difference = np.subtract(background_pixels, current_frame_pixels)

    fgmask = fgbg_extractor.apply(img)

    save_path = differential_frames_path + "/" + str(0)*(num_leading_zeros-len(str(counter))) + str(counter) + ".jpg"
    diff_img = Image.fromarray(fgmask)
    diff_img.save(save_path)

    cv2.imshow('LIVE', img)

    counter += 1

cv2.destroyAllWindows()
source.release()

ref_image = os.listdir(differential_frames_path)[0]
ref_image_name = Image.open(differential_frames_path + "/" + ref_image)
video_width, video_height = ref_image_name.size
video_fps = 12
out_path = 'data/blurred_differential_videos'
video_name = 'data/blurred_differential_videos/blurred_differential_3.mp4'

from moviepy.editor import *

def make_video(images, vid_name):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(vid_name, fourcc, video_fps, (video_width, video_height))
    for img in images:
        video.write(cv2.imread(img))
    video.release()
    print('finished '+ vid_name)

diff_images = [(differential_frames_path + "/" + f) for f in os.listdir(differential_frames_path)]

make_video(diff_images, video_name)


