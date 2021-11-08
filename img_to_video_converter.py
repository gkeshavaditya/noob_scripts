# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Keshavaditya Golla"
__email__ = "keshav.aditya19@gmail.com"

import cv2
import os

if __name__ == "__main__":

    image_folder = r"D:\py_video\2018.03.05_at_16.18.24_radar-mi_354"   # Path to images folder
    video_name = r"D:\py_video\video.avi"                               # Path to the output folder
    images = [
        img for img in os.listdir(image_folder) if img.endswith(".jpeg")
    ]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 25, (width, height))         # 25 here denotes the fps of the video

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
