import numpy as np
import cv2

def mask(img):
    ''' Function precipitation.mask.

    Detects regions of a picture whose precipitation rate is less than 1mm.
    
    Parameters:
        img (array_of_int): Picture from where low precipitation rates (< 1mm) are extracted.

    Returns:
        OutputArray (array_of_int): Mask of low precipitation rates.
    '''
    # Variables declaration
    img_hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Color range of precipitation
    lower_prec = (0, 0, 220)
    upper_prec = (50, 50, 255)
    # Mask (to select colors)
    mask = cv2.inRange(img_hsv, lower_prec, upper_prec)
    # Opening (to reduce noise)
    kernel = np.ones((3, 3), np.uint8)   # structural element
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return opening

def test():
    # Get the image
    img = cv2.imread('./data/precipitation.jpg')
    # Deal with the situation when the file is not found
    if type(img) == type(None):
        raise FileNotFoundError("<precipitation> file was not found.")
    # Apply the function "mask" on the image to create a mask
    result = mask(img)
    # Apply the mask obtained on the image and display the result
    cv2.imshow('Result', cv2.bitwise_and(img, img, mask=result))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test()