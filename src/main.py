import cv2


def main():
    """
    This function just open a specific image and write this in another dir
    with orther name to test the basic of the opencv library

    USAGE:
        from main import main

        main()
    """
    img = cv2.imread('samples/by5y3.png', 1)
    status = cv2.imwrite('./python_grey.png', img)
    print("Image written to file-system : ", status)
