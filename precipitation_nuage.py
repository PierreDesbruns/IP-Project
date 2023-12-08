import numpy as np
import cv2

def mask(img):
    ''' Function precipitation-nuage.mask.

    Detects regions of a picture where precipitation are less than 0.5mm.
    
    Parameters:
        img (array_of_int): Picture from where low precipitation or no precipitation (<0.5mm) are extracted.

    Returns:
        OutputArray (array_of_int): Mask of low precipitation or no precipitation.
    '''
    # Variables declaration
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Color range of clouds and precipitation
    lower_nuage_prec = (0, 100, 150)
    upper_nuage_prec = (162, 255, 255)
    # Mask (to select colors)
    mask = ~(cv2.inRange(img_hsv, lower_nuage_prec, upper_nuage_prec))
    # Opening (to reduce noise)
    kernel = np.ones((3, 3), np.uint8)   # structural element
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return opening

def test():
    # Get the image
    img = cv2.imread('./data/precipitation-nuage.jpg')
    # Deal with the situation when the file is not found
    if type(img) == type(None):
        raise FileNotFoundError("<precipitation-nuage> file was not found.")
    # Apply the function "mask" on the image to create a mask
    result = mask(img)
    # Apply the mask obtained on the image and display the result
    cv2.imshow('Result', cv2.bitwise_and(img, img, mask=result))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test()