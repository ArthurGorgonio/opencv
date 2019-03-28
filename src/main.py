import cv2


def main():
    """
    This function just open a specific image and write this in another dir
    with orther name to test the basic of the opencv library

    USAGE:
        from main import main

        main()
    """
    img = cv2.imread('samples/by5y3.png', 0)
    status = 0
    gauss = "./binary_gauss_"
    thresh = "./binary_threshold_"
    nogauss = "./binary_nogauss_threshold_"
    ext = ".png"

    for i in range(1, 11):
        j = ((2 * i) - 1)
        rev, thresh1 = cv2.threshold(img, 0, 255,
                                     cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        status += cv2.imwrite(nogauss + str(i) + ext, thresh1)
        img = cv2.GaussianBlur(img, (j, j), 0)
        thresh1 = cv2.adaptiveThreshold(
            img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)
        status += cv2.imwrite(gauss + str(i) + ext, thresh1)
        rev, thresh1 = cv2.threshold(img, 0, 255,
                                     cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        status += cv2.imwrite(thresh + str(i) + ext, thresh1)

    print("Image written to file-system : ", status)
