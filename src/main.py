import os

import cv2
import numpy as np


def main():
    """
    This function just open a specific image and write this in another dir
    with orther name to test the basic of the opencv library

    USAGE:
        from main import main

        main()
    """
    path = 'samples/'
    os.chdir(path)
    names = os.listdir()
    status = 0
    #    kernel = np.array(([1, 2, 1], [2, 4, 2], [1, 2, 1]), np.float32) / 16
    #    dst = cv2.filter2D(img, -1, kernel)

    for name in names:
        try:
            img = cv2.imread(name, 0)
        except FileNotFoundError:
            raise ("Path not exists")
        img = cv2.GaussianBlur(img, (7, 7), 0)
        thr = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 35, 2)
        kernel = np.ones((3, 3), np.uint8)
        dilate = cv2.dilate(thr, kernel, iterations=1)
        erose = cv2.erode(dilate, kernel, iterations=1)
        kernel = np.ones((3, 1), np.uint8)
        dilate = cv2.dilate(erose, kernel, iterations=1)
        status += cv2.imwrite("../" + name, dilate)
    print("Image written to file-system : ", status)
