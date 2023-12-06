import numpy as np
import cv2
import bitwise

def mask(img):
    ''' Function temperature.mask.
    
    Detects regions of a picture whose temperature is higher than 30°C.

    Parameters:
        img (array_of_int): Picture from where high temperatures are extracted.

    Returns:
        OutputArray (array_of_int): Mask of high temperatures.
    '''
    # Variables declaration
    masks = []
    openings = []
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Color ranges (from 30°C)
    lowerBounds = [
        (0, 50, 50),        # red
        (150, 50, 50)]      # magenta
    higherBounds = [
        (13, 255, 255),     # orange
        (179, 255, 255)]    # red
    # Mask (to select colors)
    for lowerBound, higherBound in zip(lowerBounds, higherBounds):
        masks.append(cv2.inRange(img_hsv, lowerBound, higherBound))
    # Opening (to reduce noise)
    kernel = np.ones((3, 3), np.uint8)   # structural element
    for mask in masks:
        openings.append(cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel))
    return bitwise.or_n([opening for opening in openings])
    
def test():
    img = cv2.imread('./data/temperature.jpg')
    if type(img) == type(None):
        raise FileNotFoundError("<temperature> file was not found.")
    result = mask(img);
    cv2.imshow('Result', cv2.bitwise_and(img, img, mask=result))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test()