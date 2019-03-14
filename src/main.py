import cv2


def main():
    img = cv2.imread('data/by5y3.png', 0)
    status = cv2.imwrite('./python_grey.png', img)
    print("Image written to file-system : ", status)
